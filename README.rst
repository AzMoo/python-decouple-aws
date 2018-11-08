Python Decouple AWS
===================

.. image:: https://img.shields.io/pypi/v/python-decouple-aws.svg
    :target: https://pypi.python.org/pypi/python-decouple-aws/
    :alt: Latest PyPI version


*Python Decouple AWS* helps you to organize and access sensitive information on AWS Secrets Manager.

It also makes it easy for you to:

#. Not repeat the boto3 boilerplate code;
#. Define default values;
#. Use os.environ as fall back;

Supports Python 3.4+

Why
------------

- Single place to save all secrets (AWS Secrets Manager)
- Keep sensitive information away from code and environments
- Simpler API to access AWS Secrets Manager (rather than boto3)


Installation
------------
::

    pip install python-decouple-aws


Usage example 1
---------------
::

    #  settings.py
    from decouple_aws import get_config

    # The package provides a wrapper function that will
    # fallback to environment variables and fail gracefully
    # if AWS Secrets Manager is not accessible for whatever
    # reason.
    config = get_config('your-project/secret/name', 'ap-southeast-2')

    # Use decouple config like normal
    MY_EMAIL_USER = config('MY_EMAIL_USER', 'default-user')
    MY_EMAIL_PASS = config('MY_EMAIL_PASS')


Usage example 2
---------------
::

    # settings.py
    from decouple import Config
    from decouple_aws import RepositoryAwsSecretManager

    # if you would like it to fail if secrets
    # manager is inaccessible, you can build it manually.
    # initialise the config with the AWS repository
    # Pass the repo your secret name and the region
    repo = RepositoryAwsSecretManager('your-project/secret/name', 'ap-southeast-2')
    config = Config(repo)

    # Use decouple config like normal
    MY_SUPER_SECRET_SETTING = config('MY_SUPER_SECRET_SETTING')
