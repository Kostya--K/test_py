"""
----------
Tabs tests
----------
"""

import allure

pytestmark = [
    allure.feature("DemoQA"),
    allure.story("Tabs"),
]


def test_tab2(tabs_steps):
    """**Scenario:** Verify that Tab 2 is displayed.

    Setup:

     - Launch browser and open application URL.

    Steps:

     - Open Tabs page.
     - Open Tab 2.
     - Check that Tab 2 is active.

    Teardown:

     - Close browser.
    """
    tabs_steps.open_tab2()
