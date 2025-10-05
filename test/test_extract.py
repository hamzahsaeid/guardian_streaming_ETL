import pytest
import moto
from src.extract import extract
from moto import mock_aws

"""
TDD is actually a development methodology, not just a testing system. 
It forces you to build incrementally and decide what you will write before writing.

Testing the inputs & outputs of a function

1. Test that function rejects empty string
2. Test search string, without date argument included
3. Test search argument only accepts string - test other data types
4. Test String, with date argument
5. API request returns a response
6. API request returns records
7. 

"""
def test_requests_returns_empty_dictionary_when_passed_an_empty_string():
    pass
    # Arrange
    input = ""
    # Act
    result = extract(input)
    # Assert
    assert result == {}
    

def test_extract_returns():
    pass
    # Arrange
    
    # Act
    
    # Assert
    