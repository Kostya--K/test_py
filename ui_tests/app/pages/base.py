"""
---------
Base page
---------
"""

import pom
from pom import ui
from selenium.webdriver.common.by import By

from ui_tests.app import ui as _ui


@ui.register_ui(
    menu_top=_ui.NavigateMenu(By.ID, 'menu-primary-menu'),
    menu_right=_ui.NavigateMenu(By.ID, 'secondary'),
)
class PageBase(pom.Page):
    """Base page."""

    url = '/'
    navigate_items = None

    def navigate(self, navigate_items):
        """Open page via navigation menu."""
        menu = navigate_items[0]
        getattr(self, menu).go_to(navigate_items[1:])
