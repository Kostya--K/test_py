"""
---------
Tabs page
---------
"""

from pom import ui
from selenium.webdriver.common.by import By

from ui_tests.app.pages.base import PageBase


@ui.register_ui(
    link_tab1=ui.Link(By.ID, 'ui-id-1'),
    link_tab2=ui.Link(By.ID, 'ui-id-2'),
    link_tab3=ui.Link(By.ID, 'ui-id-3'),
    tab1=ui.Block(By.ID, 'tabs-1'),
    tab2=ui.Block(By.ID, 'tabs-2'),
    tab3=ui.Block(By.ID, 'tabs-3'),
)
class PageTabs(PageBase):
    """Tabs page."""

    url = '/tabs'
    navigate_items = ('menu_top', 'Demo', 'Tabs')
