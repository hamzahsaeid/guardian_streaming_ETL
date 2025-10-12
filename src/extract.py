import boto3
import os
from botocore.exceptions import ClientError

from utils.extract_search_date import url_string
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

    # Create Secrets Manager Client
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager", region_name=region_name
    )
    # Retrieve Secret
    key_retrieval = get_secret(client, secret_name)

    # retrieve URL substring
    url_string_retrieval = url_string(search_term, date_from)

    
    guardian_url = f"https://content.guardianapis.com/search?{url_string_retrieval}&api-key={key_retrieval}"

    guardian_request = requests.get(guardian_url)
    
    if type(search_term) == str:     
        return {}
    else:
        return 'Please input a string'
    
extract("hello world")