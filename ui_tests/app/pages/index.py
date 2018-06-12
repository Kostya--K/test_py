"""
----------
Index page
----------
"""

from ui_tests.app.pages.base import PageBase


class PageIndex(PageBase):
    """Index page."""

    url = '/'
    navigate_items = ('menu_top', 'Home')
