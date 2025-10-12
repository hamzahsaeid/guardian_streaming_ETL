import pytest
import os
import requests
from unittest.mock import patch

from src.utils.get_api_data import extract_data

@pytest.fixture(scope="function", autouse=True)
def aws_credentials(): # credentials required for testing
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-north-1"


"""
- Establish successful connection to API
-
- Return dictionary of data
"""

def test_extract_data_connection_is_succesful():
    # Arrange
    url = "https://content.guardianapis.com"
    mock_response = requests.Response()
    mock_response.status_code = 200

    with patch("requests.get", return_value=mock_response):
        # Act
        response = requests.get(url)

        # Assert
        assert response.status_code == 200