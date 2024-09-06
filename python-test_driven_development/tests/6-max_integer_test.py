#!/usr/bin/python3
# 6-max_integer_test.py

import unittest

def max_integer(lst):
    """Function to find the maximum integer in a list"""
    if len(lst) == 0:
        return None
    max_int = lst[0]
    for num in lst:
        if not isinstance(num, (int, float)):
            raise TypeError("List must contain only integers or floats")
        if num > max_int:
            max_int = num
    return max_int

class TestMaxInteger(unittest.TestCase):
    def test_normal_case(self):
        """Test case with normal integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_single_element(self):
        """Test case with a single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-3]), -3)

    def test_empty_list(self):
        """Test case with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test case with floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)

    def test_mixed_numbers(self):
        """Test case with mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)
        self.assertEqual(max_integer([-1.1, 0, 2]), 2)

    def test_non_numeric(self):
        """Test case with non-numeric types"""
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3])

if __name__ == '__main__':
    unittest.main()
