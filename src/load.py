import json
import boto3
from botocore.exceptions import ClientError


def load(kinesis_client, stream_name, records):
    """Writes Guardian Records to a stream

    Given a stream name and records, writes the records
    to the steam in JSON format

    Args:
        stream_name: name of the Kinesis stream
        records: a list of dictionaries

    Returns:
        A string indicating success or a helpful error message
    """

    # confirm the stream is active
    describe = kinesis_client.describe_stream(StreamName=stream_name)
    stream_status = describe["StreamDescription"]["StreamStatus"]

    if stream_status != "ACTIVE":
        return {"ok": False, "reason": "Stream not ACTIVE",
                "status": stream_status}

    if not isinstance(records, list) or not all(isinstance(r, dict) for r in records):
        raise TypeError("The input records are not the correct data type")

    if not records:
        return "No Data to Put to Kinesis Stream"
    # Build Kinesis records
    kinesis_list = [
        {"Data": json.dumps(record).encode("utf-8"), "PartitionKey": "pk"}
        for record in records
    ]
    # Put the records into the stream
    try:
        response = kinesis_client.put_records(
            Records=kinesis_list, StreamName=stream_name
        )
        return {"Result": "Success"}
    except ClientError as e:
        return {"Error Occurred": str(e)}
