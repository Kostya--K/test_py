"""
-------------
Contact tests
-------------
"""

import allure

pytestmark = [
    allure.feature("DemoQA"),
    allure.story("Contact"),
]


def test_send_message(contact_steps):
    """**Scenario:** Verify that your message is sent successfully.

    Setup:

     - Launch browser and open application URL.

    Steps:

     - Open Contact page.
     - Fill in all fields.
     - Check that success message is displayed.

    Teardown:

     - Close browser.
    """
    contact_steps.send_message(name='user',
                               email='use@demoqa.com',
                               subject='Test subject',
                               message='Test message.')


def test_empty_email(contact_steps):
    """**Scenario:** Verify that email is required.

    Setup:

     - Launch browser and open application URL.

    Steps:

     - Open Contact page.
     - Fill in all fields except email.
     - Check that warning message is displayed.

    Teardown:

     - Close browser.
    """
    contact_steps.send_message(name='user',
                               email='',
                               subject='Test subject',
                               message='Test message.',
                               check=False)
    contact_steps.check_warning_present()
