#!/usr/bin/env python
# coding: utf-8
from __future__ import division
from hamcrest import *
import CalculatorService
import pytest

_author__ = 'kostya-karpus'


class TestCalculatorService():
    URL = 'http://api.mathjs.org/v1/'

    @pytest.fixture(scope='module')
    def idfn_x(val):
        return '(x={})'.format(str(val).replace('.', ','))

    @pytest.fixture(scope='module')
    def idfn_y(val):
        return '(y={})'.format(str(val).replace('.', ','))

    @pytest.mark.parametrize("x", [10.2, -2, 3], ids=idfn_x)
    @pytest.mark.parametrize("y", [10.2, 11, -6], ids=idfn_y)
    def test_add(self, x, y, rounding_index):
        expected_value = round(x + y, rounding_index)
        actual_value = float(CalculatorService.add(self.URL, x, y, rounding_index).get('result'))
        assert_that(actual_value, is_(expected_value),
                    "Actual value: {} doesn't equal to expected: {}".format(actual_value, expected_value))

    @pytest.mark.parametrize("x", [10.2, -2, 3], ids=idfn_x)
    @pytest.mark.parametrize("y", [10.2, 11, -6], ids=idfn_y)
    def test_divide(self, x, y, rounding_index):
        expected_value = round(float(x / y), rounding_index)
        actual_value = float(CalculatorService.divide(self.URL, x, y, rounding_index).get('result'))
        assert_that(actual_value, is_(expected_value),
                    "Actual value: {} doesn't equal to expected: {}".format(actual_value, expected_value))

    @pytest.mark.parametrize("x", [10.2, -2, 3, 2], ids=idfn_x)
    @pytest.mark.parametrize("y", [10.2, 11, -6, 0], ids=idfn_y)
    def test_multiply(self, x, y, rounding_index):
        expected_value = round(x * y, rounding_index)
        actual_value = float(CalculatorService.multiply(self.URL, x, y, rounding_index).get('result'))
        assert_that(actual_value, is_(expected_value),
                    "Actual value: {} doesn't equal to expected: {}".format(actual_value, expected_value))

    @pytest.mark.parametrize("x", [10.2, -2, 3], ids=idfn_x)
    @pytest.mark.parametrize("y", [10.2, 11, -6], ids=idfn_y)
    def test_subtract(self, x, y, rounding_index):
        expected_value = round(x - y, rounding_index)
        actual_value = float(CalculatorService.subtract(self.URL, x, y, rounding_index).get('result'))
        assert_that(actual_value, is_(expected_value),
                    "Actual value: {} doesn't equal to expected: {}".format(actual_value, expected_value))

    @pytest.mark.parametrize("x", (
            {"input": 100, "expected": '10'},
            {"input": 36, "expected": '6'}
    ), ids=idfn_x)
    def test_sqrt(self, x):
        actual_value = CalculatorService.sqrt(self.URL, x.get('input'))
        expected_value = x.get('expected')
        assert_that(actual_value, is_(expected_value),
                    "Actual value: {} doesn't equal to expected: {}".format(actual_value, expected_value))

    @pytest.mark.parametrize("x", (
            {"input": -100, "expected": "10i"},
            {"input": -36, "expected": "6i"}
    ), ids=idfn_x)
    def test_sqrt_negative(self, x):
        actual_value = CalculatorService.sqrt(self.URL, x.get('input'))
        expected_value = x.get('expected')
        assert_that(actual_value, is_(expected_value),
                    "Actual value: {} doesn't equal to expected: {}".format(actual_value, expected_value))

    @pytest.mark.parametrize("x", [10], ids=idfn_x)
    @pytest.mark.parametrize("y", [0], ids=idfn_y)
    def test_divide_zero(self, x, y, rounding_index):
        actual_value = CalculatorService.divide(self.URL, x, y, rounding_index).get('result')
        expected_value = 'Infinity'
        assert_that(actual_value, is_(expected_value),
                    "Actual value: {} doesn't equal to expected: {}".format(actual_value, expected_value))

    @pytest.mark.parametrize("x", [10], ids=idfn_x)
    @pytest.mark.parametrize("y", ["sym"], ids=idfn_y)
    def test_error_messages(self, x, y, rounding_index):
        assert_that(CalculatorService.divide(self.URL, x, y, rounding_index).get('error'),
                    has_string("Error: Undefined symbol {}".format(y)))
        
        assert_that(CalculatorService.add(self.URL, x, y, rounding_index).get('error'),
                    has_string("Error: Undefined symbol {}".format(y)))
        
        assert_that(CalculatorService.multiply(self.URL, x, y, rounding_index).get('error'),
                    has_string("Error: Undefined symbol {}".format(y)))
        
        assert_that(CalculatorService.subtract(self.URL, x, y, rounding_index).get('error'),
                    has_string("Error: Undefined symbol {}".format(y)))
        
        assert_that(CalculatorService.sqrt(self.URL, y), has_string("Error: Undefined symbol {}".format(y)))
