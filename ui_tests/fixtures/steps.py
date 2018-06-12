"""
--------------
Steps fixtures
--------------
"""

import pytest

from ui_tests.steps.contact import ContactSteps
from ui_tests.steps.tabs import TabsSteps


@pytest.fixture
def contact_steps(app):
    """Function fixture to get contact steps."""
    return ContactSteps(app)


@pytest.fixture
def tabs_steps(app):
    """Function fixture to get tabs steps."""
    return TabsSteps(app)
