#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#

import logging
import os

logger = logging.getLogger(__name__)


def create_output_folder():
    directory = "twitterbot-output"
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_output_file(filename):
    _ = open("twitterbot-output/" + filename, "w+")


def output_csv():
    pass


def output_html():
    pass


def output_json():
    pass
