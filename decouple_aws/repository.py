import json
import os

import boto3
from botocore.exceptions import BotoCoreError

from .exceptions import AWSException


class RepositoryAwsSecretManager:
    """
    Retrieves option keys from AWS Secret Manager or falls back
    to os.environ
    """
    data = {}

    def __init__(self, source, region):
        self.client = boto3.client('secretsmanager', region_name=region)
        try:
            response = self.client.get_secret_value(SecretId=source)
            parsed_secrets = json.loads(response['SecretString'])
            for k, v in parsed_secrets.items():
                self.data[k] = v
        except (self.client.exceptions.ClientError, BotoCoreError) as e:
            raise AWSException(str(e)) from e

    def __contains__(self, key):
        return key in os.environ or key in self.data

    def __getitem__(self, key):
        return self.data[key]
