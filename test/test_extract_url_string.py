import pytest
import os

from src.utils.extract_search_date import url_string


def test_url_string_requires_argument():
    # Assert
    with pytest.raises(TypeError):
        url_string()

def test_url_string_returns_one_word_when_passed_one_word():
    #Arrange
    input = "hello"
    # Act
    result = url_string(input)
    # Assert
    assert result == "hello"

def test_url_string_creates_valid_url_search_string_with_multiple_words():
    #Arrange
    input = "super duper hello"
    # Act
    result = url_string(input)
    # Assert
    assert result == '%22super%20duper%20hello%22'

def test_url_string_creates_valid_url_string_with_words_and_date_argument():
    # Arrange
    input = "super duper hello"
    date_from = '2023-01-01'
    # Act
    result = url_string(input, date_from)
    # Assert
    assert result == 'from-date=2023-01-01&q=%22super%20duper%20hello%22'

def test_url_string_requires_international_format_date_string_with_hypen_delimiter():
    # Arrange
    input = "super duper hello"
    date_from = '01-01-2024'

    # Act
    result = url_string(input,date_from)

    # Assert
    assert result == "Please enter date is correct format, as follows: YYYY-MM-DD"
