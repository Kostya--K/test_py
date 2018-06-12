"""
----------
Tabs steps
----------
"""

from hamcrest import equal_to

from ui_tests import config
from ui_tests.helpers import step
from ui_tests.helpers.matchers import check_that, returns
from ui_tests.steps.base import BaseSteps


class TabsSteps(BaseSteps):
    """Tabs page steps."""

    def _page_tabs(self):
        """Open tabs page if it is not opened."""
        return self._open(self.app.page_tabs)

    @step.step("Open tab 2")
    def open_tab2(self, check=True):
        """Step to open tab 2.

        Args:
            check (bool, optional): flag whether to check step or no

        Raises:
            AssertionError: if tab 2 will not be active
        """
        page_tabs = self._page_tabs()
        page_tabs.link_tab2.click()

        if check:
            check_that(
                lambda: page_tabs.tab2.get_attribute('aria-hidden'),
                returns(equal_to('false'), timeout=config.UI_TIMEOUT),
                "tab 2 is active")
