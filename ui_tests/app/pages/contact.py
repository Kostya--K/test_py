"""
------------
Contact page
------------
"""

from pom import ui
from selenium.webdriver.common.by import By

from ui_tests.app.pages.base import PageBase


@ui.register_ui(
    field_name=ui.TextField(By.NAME, 'your-name'),
    field_email=ui.TextField(By.NAME, 'your-email'),
    field_subject=ui.TextField(By.NAME, 'your-subject'),
    textarea_message=ui.TextField(By.NAME, 'your-message'),
    label_success_message=ui.UI(By.XPATH, './/div[contains(@class, "mail-sent-ok")]'),
    label_warning_message=ui.UI(By.XPATH, './/div[contains(@class, "validation-errors")]'),
)
class FormContact(ui.Form):
    """Contact form."""


@ui.register_ui(
    form_contact=FormContact(By.TAG_NAME, 'form'),
)
class PageContact(PageBase):
    """Contact page."""

    url = '/contact'
    navigate_items = ('menu_top', 'Contact')
