import logging
import os

logger = logging.getLogger()


def check_create_dir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
