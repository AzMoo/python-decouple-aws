import json
import os
import mock
import pytest
from botocore.exceptions import NoCredentialsError
from decouple import Config, AutoConfig, UndefinedValueError
from decouple_aws import get_config, RepositoryAwsSecretManager


def test_should_return_secrets_from_aws_secrets_manager():
    """ Test if get_config returns Config (from AWS python decouple) """

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
        is_aws_decouple = Config

        assert isinstance(config, is_aws_decouple)
        assert MY_EMAIL_USER == "user1"
        assert config('EMAIL_PASS') == '123456'


def test_should_not_fail_when_the_aws_resource_is_not_found():
    """ Test if get_config returns AutoConfig (from python decouple) as fall back """

    # Given an invalid resource name or
    #       no aws credentials

    # When
    config = get_config('invalid/resource', 'us-west-2')
    secret = config('EMAIL_USER', 'default-value')

    # Then
    is_env_decouple = AutoConfig

    assert isinstance(config, is_env_decouple)
    assert secret == 'default-value'


def test_should_return_secrets_from_aws_secrets_manager_repository():
    """
    Test if RepositoryAwsSecretManager can be instantiate direclty
    """

    with mock.patch('decouple_aws.repository.boto3') as boto3:

        # Given secrets registered on AWS
        boto3.client().get_secret_value.return_value = {
            'SecretString': json.dumps({
                'EMAIL_USER': 'user1',
                'EMAIL_PASS': '123456',
            })
        }

        # When
        repo = RepositoryAwsSecretManager('myproject/secrets1', 'ap-southeast-2')
        config = Config(repo)

        # Then the secrets should be retrieved
        assert config('EMAIL_USER') == "user1"
        assert config('EMAIL_PASS') == '123456'


def test_should_raise_NoCredentialsError_with_no_credentials():
    """ Test if users can handle errors direclty when necessary """
    # Given no Credentials

    with pytest.raises(NoCredentialsError):
        repo = RepositoryAwsSecretManager('myproject/secrets1', 'ap-southeast-2')
        config = Config(repo)

        assert repo is not None
        assert config is None


def test_should_raise_NoCredentialsError_using_the_default_api():
    """
    Test if users can handle errors direclty when necessary
    using a default api rather than be forced to instantiate RepositoryAwsSecretManager
    """
    # Given no Credentials

    with pytest.raises(NoCredentialsError):
        config = get_config('myproject/secrets', 'ap-southeast-2', fail=True)

        assert config is None


def test_should_use_environment_as_first_option():
    """ Test if ENVIRONMENT variable is the first option """
    with mock.patch('decouple_aws.repository.boto3') as boto3:

        # Given an empty secrets manager and some OS environment
        boto3.client().get_secret_value.return_value = {
            'SecretString': json.dumps({
                'MY_SECRET': 'secret-from-aws',
            })
        }
        os.environ["MY_SECRET"] = "secret-from-environment"

        # When
        config = get_config('myproject/secrets', 'ap-southeast-2')
        assert config('MY_SECRET') == "secret-from-environment"


def test_should_use_environment_with_no_aws_credentials():
    """ Test if ENVIRONMENT variable is the first option """

    # Given an empty secrets manager and some OS environment
    os.environ["MY_SECRET"] = "secret-from-environment"

    # When
    config = get_config('myproject/secrets', 'ap-southeast-2')
    assert config('MY_SECRET') == "secret-from-environment"


def test_should_raise_UndefinedValueError_for_invalid_key():

    # Given no secrets and no environment variables

    # When get_config used with no fail. Then an Exception is Raised
    with pytest.raises(UndefinedValueError):
        config = get_config('myproject/secrets1', 'ap-southeast-2')
        invalid_secret = config('MY_SECRET_NO_SET')

        assert invalid_secret is None


def test_should_use_default_value():

    # Given no secrets and no environment variables

    # When get_config used with no fail. Then an Exception is Raised
    config = get_config('myproject/secrets1', 'ap-southeast-2')
    secret = config('MY_SECRET_NO_SET', 'my-default-value')

    assert secret == 'my-default-value'
