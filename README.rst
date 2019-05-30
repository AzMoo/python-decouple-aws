Python Decouple AWS
===================

.. image:: https://img.shields.io/pypi/v/python-decouple-aws.svg
    :target: https://pypi.python.org/pypi/python-decouple-aws/
    :alt: Latest PyPI version


*Python Decouple AWS* helps you to organize and access sensitive information on AWS Secrets Manager.

It also makes it easy for you to:

#. Not repeat the boto3 boilerplate code;
#. Define default values;
#. Use os.environ when necessary;

Supports Python 3.4+

Why
------------

- Single place to save all secrets (AWS Secrets Manager)
- Keep sensitive information away from code and environments
- Simpler API to access AWS Secrets Manager (rather than boto3)
- Extention of [Python Decouple](https://github.com/henriquebastos/python-decouple)

Sequence
------------

```
                      ---> ENV ---> AWS ---> DEFAULT_VALUE
                    /
secret = config('MY_SECRET', 'my-default-value')

```

Installation
------------
::

    pip install python-decouple-aws


Usage
---------------

## Example 1

::

    #  settings.py
    from decouple_aws import get_config

    # Get the dict from AWS and make it avaible on config
    config = get_config('your-project/secret/name', 'ap-southeast-2')

    # Use decouple config like normal
    MY_EMAIL_USER = config('MY_EMAIL_USER', 'default-user')
    MY_EMAIL_PASS = config('MY_EMAIL_PASS')


## Example 2

You want to run locally or on CI server with NO AWS CREDENTIALS,
fallback to environment variables and fail gracefully
if AWS Secrets Manager is not accessible for whatever reason.

::

    $ export MY_EMAIL_PASS="MY-LOCAL-PASSWORD"

    #  settings.py
    from decouple_aws import get_config

    config = get_config('your-project/secret/name', 'ap-southeast-2')

    # Use decouple config like normal
    MY_EMAIL_USER = config('MY_EMAIL_USER', 'default-user')
    MY_EMAIL_PASS = config('MY_EMAIL_PASS')


## Example 3

You want to handle errors your self whatever reason.

::

    #  settings.py
    from decouple_aws import get_config
    from botocore.exceptions import NoCredentialsError

    config = get_config('your-project/secret/name', 'ap-southeast-2', fail=True)

    # Use decouple config like normal
    MY_SUPER_SECRET_SETTING = config('MY_SUPER_SECRET_SETTING')
                \
        It will raise NoCredentialsError
        when credentials is not found

## Example 4

whatever fail=True or failt=False, it will fail when the secret is invalid

::

    #  settings.py
    from decouple_aws import get_config
    from decouple import UndefinedValueError

    config = get_config('your-project/secret/name', 'ap-southeast-2')
    MY_SECRET = config('MY_SECRET_NOT_SET')
                   \
        It will raise UndefinedValueError
        when credentials is okay but not secret registed
