#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_max_at_end(self):
        """Test with max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with max at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with max in the middle."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative(self):
        """Test with one negative number in the list."""
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_only_negative(self):
        """Test with only negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_element(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_floats_in_list(self):
        """Test with a list that has float values."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3, 2.9]), 2.9)

    def test_mixed_list(self):
        """Test with a list of mixed types (integer and string)."""
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])

if __name__ == '__main__':
    unittest.main()
