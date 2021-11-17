#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#
# This file contains the function to retrieve
# the secrets form the config.yaml file.
#

import yaml
import logging


def read_secrets():
    """
    With this function we can read secrets
    from the configuration file.
    @return:
        {
            api_key
            api_secret_key
            bearer_token
            access_token
            access_token_secret
        }
    """
    with open("config.yaml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logger = logging.getLogger("__main__")
            logger.error(exc)
            exit()
