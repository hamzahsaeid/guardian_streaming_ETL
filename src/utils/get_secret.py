import json
import boto3
import os
from botocore.exceptions import ClientError


def get_secret(sm_client, secret_id: str):
    """Retrieves api key from AWS Secrets Manager

    Input:
        Secrets Manager client
        Secret ID - secret ID that is stored in AWS Secrets Manager

    Returns
        dictionary containing the secret string
    """

    try:
        response = sm_client.get_secret_value(SecretId=secret_id)
        decoded = json.loads(response["SecretString"])
        return decoded
    except ClientError as e:
        print(e)
        raise e

   
    