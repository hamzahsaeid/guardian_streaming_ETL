import requests
import json
import boto3
import os

"""

retrieves api key from secrets manager
connects and retrieves api data - all data or just the search data?
Returns raw data as a dictionary
"""

def extract(search_term):
    if not search_term:
        return "Please provide a search term"
    else:
        return {}
    pass
