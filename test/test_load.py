import pytest
import os
import boto3
from moto import mock_aws
from unittest.mock import patch
from botocore.exceptions import ClientError

from src.load import load


@pytest.fixture(scope="function", autouse=True)
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-north-1"


@pytest.fixture(autouse=True)
def kinesis_client():  # creates a Kinesis client & cleans up after use
    with mock_aws():
        client = boto3.client(service_name="kinesis", region_name="eu-north-1")

        response = client.create_stream(
            StreamName="test_stream",
            ShardCount=1,
            StreamModeDetails={"StreamMode": "PROVISIONED"},
        )
        yield client


def test_load_only_accepts_a_list_of_dicts_as_input_data_type(kinesis_client):
    # Arrange
    stream_name = "test_stream"
    bad_records = ([1, 2, 3], 123, {1, 2, 3}, (1, 2, 3), True, None, "hello")
    mixed_bad = [{"id": 1}, "not-a-dict"]

    # Act & Assert
    for record in bad_records:
        with pytest.raises(TypeError):
            load(kinesis_client, stream_name, record)

    with pytest.raises(TypeError):
        load(kinesis_client, stream_name, mixed_bad)

    assert (
        load(kinesis_client, stream_name, [])
        == "No Data to \
    Put to Kinesis Stream"
    )


def test_load_function_connects_to_client_and_loads_to_stream(kinesis_client):
    # Arrange
    stream_name = "test_stream"
    records = [
        {
            "webPublicationDate": "2025-06-30T18:47:23Z",
            "webTitle": "Farewell judges",
            "webUrl": "https://www.the-without-line-judges",
            "content_preview": "<p>Sometimes as absence",
        }
    ]
    # Act
    result = load(kinesis_client, stream_name, records)
    # Assert
    assert result == {"Result": "Success"}


def test_load_function_handles_error_in_put_to_kinesis_stream(kinesis_client):
    # Arrange
    stream_name = "test_stream"
    records = [{"id": "1", "title": "example"}]

    with patch("src.load.boto3.client") as mock_client:
        fake_client = mock_client.return_value
        fake_client.describe_stream.return_value = {
            "StreamDescription": {"StreamStatus": "ACTIVE"}
        }
        fake_client.put_records.side_effect = ClientError(
            {
                "Error": {
                    "Code": "ProvisionedThroughputExceededException",
                    "Message": "broken",
                }
            },
            "PutRecords",
        )

    # Act
    result = load(fake_client, stream_name, records)

    # Assert
    assert "Error Occurred" in result


def test_load_refuses_when_stream_is_not_active(kinesis_client):
    # Arrange
    stream_name = "test_stream"
    records = [{"id": "1"}]

    with patch("src.load.boto3.client") as mock_client:
        fake_client = mock_client.return_value
        fake_client.describe_stream.return_value = {
            "StreamDescription": {"StreamStatus": "CREATING"}
        }

        # Act
        result = load(fake_client, stream_name, records)

    # Assert
    assert result["ok"] is False
    assert result["reason"] == "Stream not ACTIVE"
    assert result["status"] == "CREATING"
