from decouple import AutoConfig, Config
from botocore.exceptions import BotoCoreError

from .repository import RepositoryAwsSecretManager

# We do this assertion so pyflakes doesn't complain
assert RepositoryAwsSecretManager


def get_config(source, region):
    """ Get config object but fallback to AutoConfig if AWS connection fails """
    try:
        repo = RepositoryAwsSecretManager(source, region)
        return Config(repo)
    except BotoCoreError:
        return AutoConfig()
