import pytest
from unittest.mock import patch, MagicMock
from moto import mock_aws
import boto3
import os
import requests

from src.extract import extract

@pytest.fixture(autouse=True)
def aws_credentials():  # credentials required for testing
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-north-1"

@pytest.fixture(autouse=True)
def secrets_manager(): # creates a Secrets Manager client & cleans up after use 
    with mock_aws(): 
        yield boto3.client(service_name="secretsmanager",region_name="eu-north-1")

@pytest.fixture(autouse=True)
def mocked_api_and_secrets():
    with patch("src.extract.get_secret", return_value="fake_key") as mock_get_secret, \
        patch("src.extract.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "response": {"results": [{"id": "abc", "webTitle": "test"}]}
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.raise_for_status = MagicMock()
        yield mock_get, mock_get_secret

def test_extract_function_handles_empty_results(mocked_api_and_secrets, secrets_manager):
    # Arrange
    input = "hello"
    mocked_api_and_secrets[0].return_value.json.return_value = {"response": {"results": []}}
    # Act
    assert extract(secrets_manager, input) == []

def test_extract_function_requires_a_string_argument(mocked_api_and_secrets, secrets_manager):
    input = ''
    # Assert
    with pytest.raises(TypeError):
        extract(secrets_manager,input)

def test_extract_returns_a_list_object_when_passed_a_string(mocked_api_and_secrets, secrets_manager):
    # Arrange
    input = 'hello'
    # Act
    result = extract(secrets_manager, input)
    # Assert
    assert isinstance(result, list) 

def test_extract_only_accepts_string_as_input_data_type_for_search_term(mocked_api_and_secrets, secrets_manager):
    # Arrange
    bad_inputs = ([1,2,3], 123, {1,2,3}, (1,2,3), True)
    # Act & Assert
    for input in bad_inputs:
        with pytest.raises(TypeError):    
            extract(secrets_manager, input)

def test_extract_accepts_optional_date_argument(mocked_api_and_secrets, secrets_manager):
    # Arrange
    input = "hello world"
    date_from = "2025-01-01"
    # Act
    result = extract(secrets_manager, input, date_from)
    # Assert
    assert result == [{"id": "abc", "webTitle": "test"}]

def test_extract_passed_valid_date_to_api_params(mocked_api_and_secrets, secrets_manager): 
    # Arrange
    input = "hello world"
    date_from = "2025-01-01"
     # Act
    extract(secrets_manager, input, date_from)   
     # Assert
    args, kwargs = mocked_api_and_secrets[0].call_args
    assert  kwargs["params"]["from-date"] == date_from

def test_extract_sets_page_size_to_10(mocked_api_and_secrets, secrets_manager): 
    # Arrange
    input = "hello world"
    date_from = "2025-01-01"
     # Act
    extract(secrets_manager, input, date_from)   
     # Assert
    args, kwargs = mocked_api_and_secrets[0].call_args
    assert  kwargs["params"]["page-size"] == 10

def test_url_string_requires_international_format_date_string_with_hypen_delimiter(mocked_api_and_secrets, secrets_manager):
    # Arrange
    input = "super duper hello"
    date_from = '01-01-2024'
    # Act & assert
    with pytest.raises(TypeError):
        extract(secrets_manager, input, date_from)
 
def test_extract_api_connection_returns_a_200_status_code(mocked_api_and_secrets, secrets_manager):
    # Arrange
    input = 'hello world'
    # Act
    extract(secrets_manager, input)
    # Assert
    assert mocked_api_and_secrets[0].return_value.status_code == 200

def test_extract_api_connection_handles_500_status_code(mocked_api_and_secrets, secrets_manager):
    # Arrange
    mocked_api_and_secrets[0].return_value.status_code = 500
    mocked_api_and_secrets[0].return_value.raise_for_status.side_effect = requests.HTTPError("500")
    input = 'hello world'

    # Act & assert
    with pytest.raises(requests.HTTPError):
        extract(secrets_manager, input)

def test_extract_calls_get_secrets_function_and_retrieves_the_secret(mocked_api_and_secrets, secrets_manager):
    input = 'hello world'

    # Act
    result = extract(secrets_manager, input)

    # Assert - unpacks the fixture tuple
    mocked_api_and_secrets[1].assert_called_once_with(secrets_manager, "guardian-api")