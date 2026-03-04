"""
Tests for circular_array_counter in CircularCounter.py

Run with: python -m pytest test_circular_counter.py -v

NOTE: CircularCounter.py has module-level input() calls that prevent direct import.
The function is reproduced here for testing. To fix, guard the main code in
CircularCounter.py with:  if __name__ == '__main__': ...
"""
import unittest


def circular_array_counter(array_list, skip):
    """Exact copy of the function from CircularCounter.py (without print statements)."""
    skip = skip - 1
    index = 0
    list_len = len(array_list)
    result = []
    while list_len > 0:
        index = (skip + index) % list_len
        result.append(array_list.pop(index))
        list_len -= 1
    return result


class TestCircularCounter(unittest.TestCase):

    def test_example_skip3(self):
        # Example from the docstring: [1..9] with skip=3 => 3 6 9 4 8 5 2 7 1
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(circular_array_counter(arr, 3), [3, 6, 9, 4, 8, 5, 2, 7, 1])

    def test_skip1_drains_in_order(self):
        self.assertEqual(circular_array_counter([1, 2, 3], 1), [1, 2, 3])

    def test_skip2(self):
        self.assertEqual(circular_array_counter([1, 2, 3, 4], 2), [2, 4, 3, 1])

    def test_single_element(self):
        self.assertEqual(circular_array_counter([7], 3), [7])

    def test_two_elements_skip3(self):
        self.assertEqual(circular_array_counter([1, 2], 3), [1, 2])

    def test_all_elements_removed(self):
        arr = [1, 2, 3, 4, 5]
        result = circular_array_counter(arr, 3)
        self.assertEqual(len(result), 5)
        self.assertEqual(sorted(result), [1, 2, 3, 4, 5])

    def test_modifies_original_list(self):
        # pop() empties the input list
        arr = [1, 2, 3]
        circular_array_counter(arr, 2)
        self.assertEqual(arr, [])


if __name__ == '__main__':
    unittest.main()
