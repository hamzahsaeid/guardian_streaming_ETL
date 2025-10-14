import boto3
import os
from botocore.exceptions import ClientError
import json
import re

import requests

from src.utils.get_secret import get_secret

def extract(search_term: str, date_from=None):
    """
    This function searches the Guardian API and extracts the new data
    retrieves api key from secrets manager
    connects and retrieves api data - returns the search data?
    Returns raw data as a dictionary
    """

     # secret name
    secret_name = 'guardian-api'
    region_name = 'eu-north-1'
    base_url = "https://content.guardianapis.com/search?"

    # Create Secrets Manager Client
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager", region_name=region_name
    )

    # Retrieve Secret
    key_retrieval = get_secret(client, secret_name)

    params = {
        "q": f'"{search_term}"',
        "page-size": 1,
        "show-tags": "all",
        "show-fields": "body",
        "api-key": key_retrieval
    }
    # Logic to add date_from parameter to the request params dictionary
    if date_from:
            regex = re.compile("[0-9]{4}\-[0-9]{2}\-[0-9]{2}")
            match = re.match(regex, date_from)
        
            if not (match):
                return "Please enter date is correct format, as follows: YYYY-MM-DD"
            else:
                params["from-date"]=date_from

    if type(search_term) == str:
    
        response = requests.get("https://content.guardianapis.com/search?", params=params)    
        
        data = response.json()

        results = data.get('response', {}).get('results', [])

        return results
    else:
        return 'Please input a string'
    


    
  
