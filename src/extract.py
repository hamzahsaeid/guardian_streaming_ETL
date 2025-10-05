import requests
import json
import boto3
import os

"""

retrieves api key from secrets manager
connects and retrieves api data
Returns raw data as a dictionary
"""

def extract():
    # return {}

    api_link = f"https://content.guardianapis.com/search?api-key=d1846387-ad97-4cf4-b9e4-3af7835f2b5f"
    api = requests.get(api_link)

    print(api.Response["results"])

extract()