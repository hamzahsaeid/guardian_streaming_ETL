import pytest
import boto3
from botocore.exceptions import ClientError
from moto import mock_aws
import os

from src.extract import extract


"""
TDD is actually a development methodology, not just a testing system. 
It forces you to build incrementally and decide what you will write before writing.

Testing the inputs & outputs of a function


- Test extract returns a message when empty string
- Test search argument only accepts string - test other data types
- test_extract_returns_a_dictionary_when_passed_a_string
- test extract accepts single word string
- test extract handles muti-word string
- Test search argument only accepts string - test other data types
- Test search string, without date argument
- Test String, with date argument - that it accepts the optional date
- API request returns a response
- API request returns 10 records
- Function returns JSON file


"""

@pytest.fixture(scope="function", autouse=True)
def aws_credentials(): # credentials required for testing
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-north-1"

def test_extract_returns_a_dictionary_when_passed_a_string():
    # Arrange
    input = ''
    # Act
    result = extract(input)
    # Assert
    assert result == {}
    print(result, '<<<<<<<<<<<<<<<<<<<<<<')
def test_extract_returns_a_dictionary_when_passed_a_string():
    # Arrange
    input = 'hello'
    # Act
    result = extract(input)
    # Assert
    assert result == {}

def test_extract_only_accepts_string_as_input_data_type():
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
