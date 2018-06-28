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
    from decouple_aws import RepositoryAwsSecretManager

    # initialise the config with the AWS repository
    # Pass the repo your secret name and the region
    repo = RepositoryAwsSecretManager('your/secret/name', 'ap-southeast-2')
    config = Config(repo)

    # Use decouple config like normal
    MY_SUPER_SECRET_SETTING = config('MY_SUPER_SECRET_SETTING')
