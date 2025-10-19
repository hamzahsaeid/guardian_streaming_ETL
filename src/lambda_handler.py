import boto3

from extract import extract
from transform import transform
from load import load


def lambda_handler(event, context):
    """Lambda function that runs the Extract, Transform &
    Load process & populates the named Kinesis Data Stream for
    found API data"

    Args:
      event (dict): AWS Lambda event containing:
          - "search_term" (str): the Guardian search query
          - "date_from" (str, optional): filter articles from this date
          (YYYY-MM-DD)
          - "kinesis_stream" (str): name of the target Kinesis stream
      context (dict): AWS Lambda context object (not used in this function)
    """

    # Create Kinesis and Secrets manager clients
    region = "eu-north-1"
    kenesis_client = boto3.client("kinesis", region_name=region)
    sm_client = boto3.client("secretsmanager", region_name=region)

    # call the Extract function with arguments
    raw_data = extract(sm_client, event.get("search_term"), event.get("date_from"))

    if not raw_data:
        return {
            "message": f"No results for search term: \
                {event.get("search_term")}"
        }

    # Call the transform function with the output from the
    # extract function
    transformed_data = transform(raw_data)

    # Call the load function with declared client, stream name
    # and out of transform function
    load(kenesis_client, event.get("kinesis_stream"), transformed_data)

    return {"status": "ok", "published_records": len(transformed_data)}
