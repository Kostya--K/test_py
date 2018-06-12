"""
--------------------------------
Fixtures to open web application
--------------------------------
"""

import pytest

from ui_tests.app.app import Application


@pytest.fixture
def app(variables, request):
    """Function fixture to start/stop web application."""
    app_ = Application(variables['app_url'], request.config.option.browser)
    app_.start(browser_size=variables['resolution'])

    yield app_

    app_.quit()
