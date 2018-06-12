"""
-------------
Contact steps
-------------
"""

from hamcrest import equal_to

from ui_tests import config
from ui_tests.helpers import step
from ui_tests.helpers.matchers import check_that, returns
from ui_tests.steps.base import BaseSteps


class ContactSteps(BaseSteps):
    """Contact page steps."""

    def _page_contact(self):
        """Open contact page if it is not opened."""
        return self._open(self.app.page_contact)

    @step.step("Send message '{subject}' by user '{name}'")
    def send_message(self, name, email, subject, message, check=True):
        """Step to send message.

        Args:
            name (str): name of user
            email (str): email of user
            subject (str): subject of message
            message (str): message
            check (bool, optional): flag whether to check step or no

        Raises:
            AssertionError: if success message is not displayed
        """
        page_contact = self._page_contact()
        with page_contact.form_contact as form:
            form.field_name.set_value(name)
            form.field_email.set_value(email)
            form.field_subject.set_value(subject)
            form.textarea_message.set_value(message)
            form.submit()

            if check:
                check_that(
                    lambda: form.label_success_message.is_present,
                    returns(equal_to(True), timeout=config.UI_TIMEOUT),
                    "success message is displayed")

    @step.step("Check warning message is present")
    def check_warning_present(self):
        """Step to check warning message is present."""
        self._page_contact().form_contact.label_warning_message.wait_for_presence()
