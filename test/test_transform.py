import pytest
import moto
from src.extract import extract
from moto import mock_aws

"""


"""
def test_requests_returns_a_message_when_passed_an_empty_string():
    # Arrange
    input = ""
    # Act
    result = extract(input)
    # Assert
    assert result == "Please provide a search term"
    

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
    assert result1 