"""
Tests for binary_search.py

Run with: python -m pytest test_binary_search.py -v
      or: python -m unittest test_binary_search
"""
import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from binary_search import binary_search


ARR = [2, 4, 6, 8, 15, 30, 55, 70, 100]


class TestBinarySearchFound(unittest.TestCase):

    def test_first_element(self):
        self.assertEqual(binary_search(ARR, 2), 0)

    def test_second_element(self):
        self.assertEqual(binary_search(ARR, 4), 1)

    def test_middle_element(self):
        self.assertEqual(binary_search(ARR, 8), 3)

    def test_element_at_index_4(self):
        self.assertEqual(binary_search(ARR, 15), 4)

    def test_element_at_index_5(self):
        self.assertEqual(binary_search(ARR, 30), 5)

    def test_element_at_index_6(self):
        self.assertEqual(binary_search(ARR, 55), 6)

    def test_element_at_index_7(self):
        self.assertEqual(binary_search(ARR, 70), 7)

    def test_last_element(self):
        self.assertEqual(binary_search(ARR, 100), 8)


class TestBinarySearchNotFound(unittest.TestCase):

    def test_value_below_all(self):
        self.assertEqual(binary_search(ARR, 1), -1)

    def test_value_between_index_0_and_1(self):
        self.assertEqual(binary_search(ARR, 3), -1)

    def test_value_between_index_1_and_2(self):
        self.assertEqual(binary_search(ARR, 5), -1)

    def test_value_between_index_2_and_3(self):
        self.assertEqual(binary_search(ARR, 7), -1)

    def test_value_not_in_upper_half(self):
        self.assertEqual(binary_search(ARR, 10), -1)

    def test_value_above_all(self):
        self.assertEqual(binary_search(ARR, 999), -1)


class TestBinarySearchEdgeCases(unittest.TestCase):

    def test_single_element_found(self):
        self.assertEqual(binary_search([42], 42), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([42], 7), -1)

    def test_two_elements_first(self):
        self.assertEqual(binary_search([1, 3], 1), 0)

    def test_two_elements_second(self):
        self.assertEqual(binary_search([1, 3], 3), 1)


if __name__ == '__main__':
    unittest.main()
