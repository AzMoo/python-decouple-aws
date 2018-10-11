import json
import os
import mock
from decouple_aws import get_config


def test_should_return_secrets_from_aws_secrets_manager():
    with mock.patch('decouple_aws.repository.boto3') as boto3:

        # Given secrets registered on AWS
        boto3.client().get_secret_value.return_value = {
            'SecretString': json.dumps({
                'EMAIL_USER': 'user1',
                'EMAIL_PASS': '123456',
            })
        }

        # When
        config = get_config('myproject/secrets1', 'ap-southeast-2')
        MY_EMAIL_USER = config('EMAIL_USER')

        # Then the secrets should be retrieved
        assert MY_EMAIL_USER == "user1"
        assert config('EMAIL_PASS') == '123456'


def test_should_use_environment_as_fall_back():
    with mock.patch('decouple_aws.repository.boto3') as boto3:

        # Given an empty secrets manager and some OS environment
        boto3.client().get_secret_value.return_value = {
            'SecretString': json.dumps({})
        }
        os.environ["EMAIL_USER"] = "user-test"

        # When
        config = get_config('myproject/secrets1', 'ap-southeast-2')
        assert config('EMAIL_USER') == "user-test"
