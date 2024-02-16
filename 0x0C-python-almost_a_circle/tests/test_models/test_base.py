#!/usr/bin/python3
'''
This contains the test class for the ``Base`` class

'''
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''
    Unit testing the base class
    '''
    def test_an_instant_no_arg(self):
        '''
        test instantiation with no argument
        '''
        b = Base()
        self.assertEqual(b.id, 1)

    def test_instant(self):
        '''
        running test
        '''
        b1 = Base()
        b2 = Base(0)
        cls = b1.__class__
        self.assertEqual(cls.__name__, 'Base')
        self.assertEqual(b1.id, 3)
        self.assertEqual(b2.id, 0)
        self.assertRaises(TypeError, Base, None, 2)

    def test_nb_objects(self):
        '''
        running test
        '''
        self.assertEqual(hasattr(Base, '__nb_objects'), False)


    def test_given_id(self):
        '''
        running test
        '''
        b = Base(13)
        self.assertEqual(b.id, 13)

    def test_negative_id(self):
        '''
        running test
        '''
        b = Base(-2)
        self.assertEqual(b.id, -2)

    def test_id(self):
        '''
        running test
        '''
        self.assertEqual(hasattr(Base(), 'id'), True)

    def test_to_json_type(self):
        """
           test to_json type
        """
        sq = Square(9)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        sq = Square(1, 0, 0, 9)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string), [{"id": 9, "y": 0,
                                                    "size": 1, "x": 0}])
    def test_to_json_None(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_empty(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        sq = Square(1, 0, 0, 234)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        json_list = Base.from_json_string(json_string)
        self.assertEqual(json_list, [{'size': 1, 'x': 0, 'y': 0, 'id': 234}])

    def test_from_json_none(self):
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_from_json_empty(self):
        json_list = Base.from_json_string([])
        self.assertEqual(json_list, [])



if __name__ == '__main__':
    unittest.main()
