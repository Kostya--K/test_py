"""
--------------
Step decorator
--------------
"""

import allure
from pom import utils


def step(obj):
    """Decorator over 'allure.step' and 'logger.log'."""

    def wrapper(func):
        return allure_step(utils.log(func))

    if callable(obj):
        allure_step = allure.step
        return wrapper(obj)
    else:
        allure_step = allure.step(obj)
        return wrapper
