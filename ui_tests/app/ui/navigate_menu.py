"""
-------------
Navigate menu
-------------
"""

from pom import ui, utils
from selenium.webdriver.common.by import By


class NavigateMenu(ui.Block):
    """Navigate menu."""

    _item_selector = './/a[contains(., "{}")]'
    _sub_container_selector = './parent::*'

    @utils.log
    def go_to(self, item_names):
        """Go to page via navigate menu.
        Args:
            item_names: list of items of navigate menu.
        """
        container = self

        item = None
        parent_item = None

        for item_name in item_names:
            item = ui.Block(By.XPATH, self._item_selector.format(item_name))
            item.set_container(container)

            if not item.is_present and parent_item:
                parent_item.click()
                item.wait_for_presence()

            container = ui.Block(By.XPATH, self._sub_container_selector)
            container.set_container(item)
            parent_item = item

        item.click()
