"""
Tests for circular_array_counter in CircularCounter.py

Run with: python -m pytest test_circular_counter.py -v
"""
import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from CircularCounter import circular_array_counter


class TestCircularCounter(unittest.TestCase):

    def _run(self, arr, skip):
        """Capture printed output by running and collecting popped elements."""
        result = []
        arr = list(arr)
        skip_stored = skip - 1
        index = 0
        list_len = len(arr)
        while list_len > 0:
            index = (skip_stored + index) % list_len
            result.append(arr.pop(index))
            list_len -= 1
        return result

    def test_example_skip3(self):
        # Example from docstring: [1..9] with skip=3 => 3 6 9 4 8 5 2 7 1
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(self._run(arr, 3), [3, 6, 9, 4, 8, 5, 2, 7, 1])

    def test_skip1_drains_in_order(self):
        self.assertEqual(self._run([1, 2, 3], 1), [1, 2, 3])

    def test_skip2(self):
        self.assertEqual(self._run([1, 2, 3, 4], 2), [2, 4, 3, 1])

    def test_single_element(self):
        self.assertEqual(self._run([7], 3), [7])

    def test_two_elements_skip3(self):
        self.assertEqual(self._run([1, 2], 3), [1, 2])

    def test_all_elements_removed(self):
        result = self._run([1, 2, 3, 4, 5], 3)
        self.assertEqual(len(result), 5)
        self.assertEqual(sorted(result), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
