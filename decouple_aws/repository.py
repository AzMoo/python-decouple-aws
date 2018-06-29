import json
import os

import boto3


class RepositoryAwsSecretManager(object):
    """
    Retrieves option keys from AWS Secret Manager or falls back
    to os.environ
    """
    data = {}

    def __init__(self, source, region):
        self.client = boto3.client('secretsmanager', region_name=region)
        response = self.client.get_secret_value(SecretId=source)
        parsed_secrets = json.loads(response['SecretString'])
        for k, v in parsed_secrets.items():
            self.data[k] = v

    def __contains__(self, key):
        return key in os.environ or key in self.data

    def __getitem__(self, key):
        return self.data[key]
