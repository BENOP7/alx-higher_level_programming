#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_diff_lists(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 2, 9, 8, 0]), 9)
        self.assertEqual(max_integer([6, 3, 5, 2, 4]), 6)
        self.assertEqual(max_integer([4, 5, 1, 2, 5]), 5)
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3)
        self.assertEqual(max_integer([3]), 3)

    def test_non_integer_lists(self):
        self.assertRaises(TypeError, max_integer, [1, 'a', 2, 'b', 3, 'c'])
        self.assertEqual(max_integer(['A', 'b', 'C', 'd', 'E']), 'd')
        self.assertRaises(TypeError, max_integer, ['A', 2, 3, 4])

    def test_empty_sequence(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer({}), None)
        self.assertEqual(max_integer(set()), None)
        self.assertEqual(max_integer(range(0)), None)
        self.assertEqual(max_integer(b''), None)
        self.assertEqual(max_integer(''), None)
        self.assertEqual(max_integer(), None)

    def test_tuple(self):
        self.assertEqual(max_integer((1, 3, 0)), 3)

    def test_set(self):
        self.assertRaises(TypeError, max_integer, set([5, 3, 0, 5, 3]))

    def test_range_type(self):
        self.assertEqual(max_integer(range(10, 0, -2)), 10)

    def test_dict(self):
        self.assertRaises(KeyError, max_integer,
                          {0: '1', 4: '2', 2: '3', 3: '4'})
        self.assertEqual(max_integer({0: '1', 1: '2', 2: '3', 3: '4'}), '4')

    def test_other_types(self):
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, False)
        self.assertRaises(TypeError, max_integer, 3)
        self.assertRaises(TypeError, max_integer, 1.2)
        self.assertRaises(TypeError, max_integer, 3 + 2j)
