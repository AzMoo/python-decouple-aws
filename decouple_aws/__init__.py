import logging

from decouple import AutoConfig, Config

from .exceptions import AWSException
from .repository import RepositoryAwsSecretManager

# We do this assertion so pyflakes doesn't complain
assert RepositoryAwsSecretManager

logger = logging.getLogger(__name__)


def get_config(source, region):
    """ Get config object but fallback to AutoConfig if AWS connection fails"""
    try:
        logger.debug(
            'Querying AWS Secrets manager for %s in region %s', source, region)
        repo = RepositoryAwsSecretManager(source, region)
        logger.debug('Successfully queried for %s in region %s',
                     source, region)
        return Config(repo)
    except AWSException as e:
        logger.error(
            'Failed retrieving secrets from AWS Secrets Manager: %s', e)
        return AutoConfig()
