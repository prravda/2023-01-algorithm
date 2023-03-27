import unittest
from typing import TypedDict

from solution_v0 import solution


class TestSuiteForKthSmallValue(TypedDict):
    list_of_int: list[int]
    sum_result: int


test_suites: list[TestSuiteForKthSmallValue] = [
    {'list_of_int': [9, 1, 3, 2, 7, 0, -2, 4, 5], 'sum_result': 19},
    {'list_of_int': [7, 6, 5, 4, 3, 2, 1], 'sum_result': 33},
    {'list_of_int': [11, 12, -20, 14, -10, -8, -7, -6, -4, -2], 'sum_result': -38},
]


class TestFunctionForKthSmallValue(unittest.TestCase):
    def test_each_suite(self):
        for each_case in test_suites:
            result = solution(each_case['list_of_int'])
            self.assertEqual(each_case['sum_result'], result)
