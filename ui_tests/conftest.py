"""
---------------
Global conftest
---------------
"""

import allure

pytest_plugins = [
    'ui_tests.fixtures.app',
    'ui_tests.fixtures.report',
    'ui_tests.fixtures.steps',
    'ui_tests.fixtures.video',
]


def pytest_addoption(parser):
    """Add options to pytest."""
    parser.addoption("--enable-virtual-display", action="store_true",
                     help="Enable virtual display")
    parser.addoption("--enable-video-capture", action="store_true",
                     help="Enable video capture")
    parser.addoption("--browser", action='store',
                     choices=['chrome', 'firefox', 'remote'],
                     help="Browser to launch web app")


def pytest_exception_interact(node, call, report):
    if 'app' in node.funcargs:
        app = node.funcargs['app']
        allure.attach(app.webdriver.get_screenshot_as_png(),
                      'screenshot',
                      allure.attachment_type.PNG)
