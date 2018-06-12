"""
---------------
Report fixtures
---------------
"""

import logging
import logging.config
import os

import allure
import pytest
import yaml

from ui_tests import config
from ui_tests.helpers import utils


@pytest.fixture
def report_dir(request):
    """Function fixture to create report directory.

    Args:
        request (object): pytest request

    Returns:
        str: path to report directory
    """
    report_dir_ = os.path.join(config.TEST_REPORTS_DIR,
                               utils.slugify(request.node.name))

    if not os.path.isdir(report_dir_):
        os.makedirs(report_dir_)

    return report_dir_


@pytest.fixture(autouse=True)
def report_log(report_dir):
    """Autouse function fixture to configure log handlers to write test logs.

    Args:
        report_dir (str): path to report directory
    """
    log_path = os.path.join(report_dir, 'called_functions.log')
    yaml_path = os.path.join(os.path.dirname(__file__), 'logging.yaml')
    with open(yaml_path) as file:
        log_content = file.read().format(FILE_PATH=log_path)
    logging.config.dictConfig(yaml.safe_load(log_content))

    yield

    with open(log_path) as log_file:
        allure.attach(log_file.read(),
                      'called functions',
                      allure.attachment_type.TEXT)
