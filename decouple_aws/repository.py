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
        for k, v in response['SecretString']:
            self.data[k] = v

    def __contains__(self, key):
        return key in os.environ or key in self.stored_secrets

    def __getitem__(self, key):
        return self.data[key]
