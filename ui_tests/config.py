"""
------
Config
------
"""

import os

UI_TIMEOUT = 5
PAGE_TIMEOUT = 30

TEST_REPORTS_DIR = os.environ.get(
    "TEST_REPORTS_DIR",
    os.path.join(os.getcwd(),  # put results to folder where tests are launched
                 "test_reports"))

XVFB_LOCK = "/tmp/cases_xvfb.lock"
