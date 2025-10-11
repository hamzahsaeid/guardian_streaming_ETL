import pytest
import boto3
from botocore.exceptions import ClientError
from src.utils.get_secret import get_secret
from moto import mock_aws
import os

"""
- Test valid aws Secret is retrieved
- Test invlaid aws Secret retrieval
"""


@pytest.fixture(scope="function")
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


def test_get_secret_retrieves_valid_secret(aws_credentials):
    # Arrange
    with mock_aws():
        test_client = boto3.client("secretsmanager")
        test_client.create_secret(
            Name="guardian-api",
            SecretString='{"key": "guardian","value": "hello"}'
        )
    # Act
        expected_response = {'key': 'guardian','value': 'hello'}
        result = get_secret(test_client, "guardian-api")
        # Assert
        assert result == expected_response
    

def test_extract_returns_a_dictionary_when_passed_a_string():
    # Arrange
    with mock_aws():
        test_client = boto3.client("secretsmanager")
        test_client.create_secret(
            Name="broken_secret",
            SecretString='{"key": "broken","value": "down"}'
        )
    # Act
    with pytest.raises(ClientError):
        get_secret(test_client, "guardian_api")
    # Assert