"""
------------------------
Custom hamcrest matchers
------------------------
"""

import allure
import waiting
from hamcrest import assert_that
from hamcrest.core.base_matcher import BaseMatcher


def check_that(actual, matcher, message):
    """Wrapper over 'assert_that' to add step in allure report."""
    __tracebackhide__ = True
    with allure.step("Check that " + message):
        assert_that(actual, matcher, message)


class Returns(BaseMatcher):
    """Matcher to check that a result is being matched during timeout."""

    def __init__(self, matcher, timeout):
        self.matcher = matcher
        self.timeout = timeout
        self.last_result = None

    def _matches(self, func):

        def f():
            self.last_result = func()
            return self.matcher.matches(self.last_result)

        try:
            return waiting.wait(f,
                                timeout_seconds=self.timeout,
                                sleep_seconds=0.1)
        except waiting.TimeoutExpired:
            return False

    def describe_to(self, description):
        description.append_description_of(self.matcher).append_text(
            ' during {} sec.'.format(self.timeout))

    def describe_mismatch(self, func, description):
        self.matcher.describe_mismatch(self.last_result, description)


def returns(matcher, timeout):
    return Returns(matcher, timeout)
