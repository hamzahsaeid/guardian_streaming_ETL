import boto3

from src.extract import extract
from src.transform import transform
from src.load import load

def cli(search_term: str, kinesis_stream: str, date_from=None):
    """ Command Line function that runs the Extract, Transform and Load process and
    populates the named Kinesis Data Stream for found API data"

    Args:
      search_term:
      kinesis_stream:
      date_from: 
    
    """
    
    # Create Kinesis and Secrets manager clients
    region = 'eu-north-1'
    kenesis_client = boto3.client("kinesis",region_name=region)
    sm_client = boto3.client("secretsmanager", region_name=region)

    # call the extract, transform and load
    raw_data = extract(sm_client, search_term, date_from)

    if not raw_data:
        return print({"message": f"No results for search term: {search_term}"})

    # Call the transform function with the output from the extract function
    transformed_data = transform(raw_data)

    # Call the load function with declared client, stream name and out of transform function 
    load(kenesis_client, kinesis_stream, transformed_data )