"""
-----------
Application
-----------
"""

import tempfile

import pom
from pom import ui
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui_tests import config
from ui_tests.app import pages

ui.UI.timeout = config.UI_TIMEOUT
RemoteConnection.set_timeout(config.PAGE_TIMEOUT)


@pom.register_pages(pages.pages)
class Application(pom.App):
    """Web application.

    Args:
        url (str): URL of web application.
        browser (str): Name of browser to launch.
        *args: Selenium arguments.
        **kwgs: Selenium keyword arguments.
    """

    def __init__(self, url, browser, *args, **kwgs):
        profile_dir = tempfile.mkdtemp()

        if browser == 'chrome':
            kwgs['executable_path'] = ChromeDriverManager().install()
            options = webdriver.ChromeOptions()
            options.add_argument("user-data-dir=" + profile_dir)
            kwgs['chrome_options'] = options

        if browser == 'firefox':
            kwgs['executable_path'] = GeckoDriverManager().install()
            profile = webdriver.FirefoxProfile(profile_dir)
            kwgs['firefox_profile'] = profile

        if browser == 'remote':
            kwgs['command_executor'] = 'http://127.0.0.1:4444/wd/hub'
            options = webdriver.ChromeOptions()
            kwgs['desired_capabilities'] = options.to_capabilities()

        super(Application, self).__init__(url=url, browser=browser, *args, **kwgs)

    def start(self, browser_size=None):
        """Launch browser.

        Args:
            browser_size (tuple, optional): browser size.
        """
        if browser_size:
            self.webdriver.set_window_size(*browser_size)
        self.webdriver.set_page_load_timeout(config.PAGE_TIMEOUT)
        self.webdriver.get(self.app_url)
