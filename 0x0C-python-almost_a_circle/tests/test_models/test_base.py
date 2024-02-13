'''
This contains the test class for the ``Base`` class

'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''
    Unit testing the base class
    '''
    def test_an_instant_no_arg(self):
        b = Base()
        assertEqual(b.id, 1)

    def test_instant(self):
        '''
        running test
        '''
        b1 = Base()
        b2 = Base(0)
        cls = b1.__class__
        self.assertEqual(cls.__name__, 'Base')
        self.assertEqual(b1.id, 2)
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


if __name__ == '__main__':
    unittest.main()
