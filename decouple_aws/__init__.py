import logging

from decouple import AutoConfig, Config
from botocore.exceptions import ClientError, BotoCoreError

from .repository import RepositoryAwsSecretManager

# We do this assertion so pyflakes doesn't complain
assert RepositoryAwsSecretManager

logger = logging.getLogger(__name__)


def get_config(source, region, fail=False):
    """ Get config object but fallback to AutoConfig if AWS connection fails"""
    try:
        logger.debug(
            'Querying AWS Secrets manager for %s in region %s', source, region)
        repo = RepositoryAwsSecretManager(source, region)
        logger.debug('Successfully queried for %s in region %s',
                     source, region)
        return Config(repo)

    except (ClientError, BotoCoreError) as e:
        if fail:
            raise e
        logger.error(
            'Failed retrieving secrets from AWS Secrets Manager: %s', e)
        return AutoConfig()
