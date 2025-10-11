import requests
import json
import boto3
import os
from botocore.exceptions import ClientError

def extract(search_term: str):
    """
    Checks for updates in the Guardian API and extracts the new data
    retrieves api key from secrets manager
    connects and retrieves api data - all data or just the search data?
    Returns raw data as a dictionary
    """

    """
    - Create SM client
    - Connect to API
    """

 
    if not search_term or not type(search_term) == str:
        return "Please input a string"
    else:
        return {}