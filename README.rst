Python Decouple AWS
===================

AWS Extensions for Python Decouple

Installation
------------
::

    pip install python-decouple-aws


Usage
-----
::

    # Import
    from decouple import Config
    from decouple_aws import get_config, RepositoryAwsSecretManager

    # The package provides a wrapper function that will
    # fallback to environment variables and fail gracefully
    # if AWS Secrets Manager is not accessible for whatever
    # reason.
    config = get_config('your/secret/name', 'ap-southeast-2')

    # Alternatively, if you would like it to fail if secrets
    # manager is inaccessible, you can build it manually.
    # initialise the config with the AWS repository
    # Pass the repo your secret name and the region
    repo = RepositoryAwsSecretManager('your/secret/name', 'ap-southeast-2')
    config = Config(repo)

    # Use decouple config like normal
    MY_SUPER_SECRET_SETTING = config('MY_SUPER_SECRET_SETTING')
