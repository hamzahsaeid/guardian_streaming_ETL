import pytest
import requests_new
from unittest.mock import patch

from src.extract import extract

"""
- API request returns a response  
- API handles failed response
- API request returns 10 records
"""

@pytest.fixture(autouse=True)
def patch_external_services():
    with patch("src.utils.get_secret.get_secret", return_value="fake_key"), \
        patch("src.extract.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "response": {"results": [{"id": "abc", "webTitle": "test"}]}
        }
        mock_get.return_value.status_code = 200
        yield mock_get

def test_extract_function_requires_a_string_argument():
    # Assert
    with pytest.raises(TypeError):
        extract()

def test_extract_returns_a_list_object_when_passed_a_string():
    # Arrange
    input = 'hello'
    # Act
    result = extract(input)
    # Assert
    assert type(result) == list

def test_extract_only_accepts_string_as_input_data_type_for_search_term():
    # Arrange
    input1 = [1,2,3]
    input2 = 123
    input3 = {1,2,3}
    input4 = (1,2,3)
    input5 = True
    # Act
    result1 = extract(input1)
    result2 = extract(input2)
    result3 = extract(input3)
    result4 = extract(input4)
    result5 = extract(input5)
    #Assert
    assert result1 == "Please input a string"
    assert result2 == "Please input a string"
    assert result3 == "Please input a string"
    assert result4 == "Please input a string"
    assert result5 == "Please input a string"

def test_extract_accepts_optional_date_argument(patch_external_services):
    # Arrange
    input = "hello world"
    date_from = "2025-01-01"
    # Act
    result = extract(input, date_from)
    # Assert
    assert result == [{"id": "abc", "webTitle": "test"}]

def test_url_string_requires_international_format_date_string_with_hypen_delimiter():
    # Arrange
    input = "super duper hello"
    date_from = '01-01-2024'

    # Act
    result = extract(input,date_from)

    # Assert
    assert result == "Please enter date is correct format, as follows: YYYY-MM-DD"
 
def test_extract_api_connection_returns_a_200_status_code(patch_external_services):
    # Arrange
    input = 'hello world'

    # Act
    result = extract(input)

    # Assert
    assert patch_external_services.return_value.status_code == 200