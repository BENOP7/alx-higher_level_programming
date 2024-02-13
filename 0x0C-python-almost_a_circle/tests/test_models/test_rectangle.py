#!/usr/bin/python3
'''
Contains the TestRectangle class for the unit testing of the
Rectangle class
'''
import sys
import unittest as ut
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(ut.TestCase):
    '''
    unittest class for the Rectangle model
    '''
    def setUpClass():
        TestRectangle.tmp_id = 0

    def test_type(self):
        r = Rectangle(3, 2)
        self.assertTrue(isinstance(r, Rectangle))
        self.assertTrue(issubclass(r.__class__, Base))

    def test_instant(self):
        r = Rectangle(4, 2, 0, 0, 13)
        self.assertEqual(r.id, 13)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(3)
        with self.assertRaises(TypeError):
            r = Rectangle(3, 2, 1, 1, 0, "inf")

    def test_nb_objects(self):
        self.assertFalse(hasattr(Rectangle, '__nb_objects'))

    def test_id_none(self):
        r = Rectangle(2, 2, 0, 0, -5)
        self.assertEqual(r.id, -5)
        r = Rectangle(2, 2, 0, 0, None)
        TestRectangle.tmp_id = r.id
        r = Rectangle(2, 3, 0, 2)
        TestRectangle.tmp_id += 1
        self.assertEqual(r.id, TestRectangle.tmp_id)
        r = Rectangle(2, 3, 0, 2)
        TestRectangle.tmp_id += 1
        self.assertEqual(r.id, TestRectangle.tmp_id)

    def test_width(self):
        r = Rectangle(2, 1)
        self.assertTrue(hasattr(r, 'width'))
        self.assertFalse(hasattr(r, '__width'))
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        with self.assertRaises(TypeError):
            r = Rectangle(None, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 3)
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 3)
        with self.assertRaises(TypeError):
            r = Rectangle('4', 3)
        with self.assertRaises(TypeError):
            r = Rectangle(2.2, 3)

    def test_height(self):
        r = Rectangle(2, 1)
        self.assertTrue(hasattr(r, 'height'))
        self.assertFalse(hasattr(r, '__height'))
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(2, None)
        with self.assertRaises(ValueError):
            r = Rectangle(3, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(3, -3)
        with self.assertRaises(TypeError):
            r = Rectangle(4, '3')
        with self.assertRaises(TypeError):
            r = Rectangle(3, 2.2)

    def test_x(self):
        r = Rectangle(2, 1, 3)
        self.assertTrue(hasattr(r, 'x'))
        self.assertFalse(hasattr(r, '__x'))
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 2, None, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(3, 2, -1, 0)
        r = Rectangle(5, 3, 0, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(3, 3, '4')

    def test_y(self):
        r = Rectangle(2, 1, 3, 2)
        self.assertTrue(hasattr(r, 'y'))
        self.assertFalse(hasattr(r, '__y'))
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 2)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 2, 0, None)
        with self.assertRaises(ValueError):
            r = Rectangle(3, 2, 0, -1)
        r = Rectangle(5, 3, 1, 0)
        with self.assertRaises(TypeError):
            r = Rectangle(3, 2, 1, '4')

    def test_width_setter(self):
        r = Rectangle(2, 1)
        r.width = 1
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        with self.assertRaises(TypeError):
            r = Rectangle(1, 2)
            r.width = None
        with self.assertRaises(ValueError):
            r = Rectangle(1, 3)
            r.width = -1
        with self.assertRaises(ValueError):
            r = Rectangle(1, 3)
            r.width = 0
        with self.assertRaises(TypeError):
            r = Rectangle(4, 3)
            r.width = '7'
        with self.assertRaises(TypeError):
            r = Rectangle(1, 3)
            r.width = 2.2

    def test_height_setter(self):
        r = Rectangle(2, 1)
        self.assertEqual(r.width, 2)
        r.height = 2
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(3, 1)
            r.height = 0
            r.height = -1
        with self.assertRaises(TypeError):
            r = Rectangle(3, 2)
            r.height = None
            r.height = []
            r.height = 2.2
            r.height = True

    def test_x_setter(self):
        r = Rectangle(3, 2, 0, 3)
        r.x = 2
        self.assertEqual(r.x, 2)
        r.x = 0
        self.assertEqual(r.x, 0)

        with self.assertRaises(TypeError):
            r.x = None
        with self.assertRaises(TypeError):
            r.x = False
        with self.assertRaises(TypeError):
            r.x = [1, 2]
        with self.assertRaises(TypeError):
            r.x = 3.3
        with self.assertRaises(TypeError):
            r.x = ()
        with self.assertRaises(TypeError):
            r.x = {}
        with self.assertRaises(ValueError):
            r = Rectangle(3, 4)
            r.x = -1

    def test_y_setter(self):
        r = Rectangle(3, 2, 0, 3)
        r.y = 2
        self.assertEqual(r.y, 2)
        r.y = 0
        self.assertEqual(r.y, 0)

        with self.assertRaises(TypeError):
            r.y = None
        with self.assertRaises(TypeError):
            r.y = False
        with self.assertRaises(TypeError):
            r.y = [1, 2]
        with self.assertRaises(TypeError):
            r.y = 3.3
        with self.assertRaises(TypeError):
            r.y = ()
        with self.assertRaises(TypeError):
            r.y = {}
        with self.assertRaises(ValueError):
            r = Rectangle(3, 4)
            r.y = -1

    def test_area(self):
        r = Rectangle(4, 3)
        self.assertEqual(r.area(), 12)
        r.width = 50
        r.height = 20
        self.assertEqual(r.area(), 1000)
        self.assertRaises(TypeError, r.area, 'area')
        self.assertRaises(TypeError, r.area, 1, 'area')
        self.assertRaises(TypeError, r.area, [])
        self.assertRaises(TypeError, r.area, {})
        self.assertRaises(TypeError, r.area, True, 0, 2.3)

    def test_display(self):
        r = Rectangle(4, 3)
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), '####\n####\n####\n')
        with self.assertRaises(TypeError):
            r.display(2)

    def test_display_xy(self):
        r = Rectangle(2, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        self.assertEqual(captured_output.getvalue(), '  ##\n  ##\n')
        sys.stdout.close()
        captured_output = StringIO()
        sys.stdout = captured_output
        r.y = 2
        r.x = 0
        r.display()
        self.assertEqual(captured_output.getvalue(), '\n\n##\n##\n')
        sys.stdout.close()
        captured_output = StringIO()
        sys.stdout = captured_output
        r.x = 1
        r.width = 4
        r.display()
        self.assertEqual(captured_output.getvalue(), '\n\n ####\n ####\n')
        sys.stdout.close()
        sys.stdout = sys.__stdout__

    def test_str(self):
        r = Rectangle(1, 2, 3, 4, 76)
        self.assertEqual("[Rectangle] (76) 3/4 - 1/2", r.__str__())

    def test_update(self):
        r = Rectangle(5, 5, 5, 5, -2)
        self.assertEqual(r.__str__(), '[Rectangle] (-2) 5/5 - 5/5')
        r.update()
        self.assertEqual(r.__str__(), '[Rectangle] (-2) 5/5 - 5/5')
        r.update(0)
        self.assertEqual(r.__str__(), '[Rectangle] (0) 5/5 - 5/5')
        r.update(0, 1)
        self.assertEqual(r.__str__(), '[Rectangle] (0) 5/5 - 1/5')
        r.update(0, 1, 2)
        self.assertEqual(r.__str__(), '[Rectangle] (0) 5/5 - 1/2')
        r.update(0, 1, 2, 3)
        self.assertEqual(r.__str__(), '[Rectangle] (0) 3/5 - 1/2')
        r.update(0, 1, 2, 3, 4)
        self.assertEqual(r.__str__(), '[Rectangle] (0) 3/4 - 1/2')

    def test_update_exc(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.update(1, None)
        with self.assertRaises(TypeError):
            r.update(1, 2, False)       
        with self.assertRaises(TypeError):
            r.update(1, 2, 3, 3.5)
        with self.assertRaises(TypeError):
            r.update(1, 2, 3, 4, [])
        with self.assertRaises(ValueError):
            r.update(1, -2)
        with self.assertRaises(ValueError):
            r.update(1, 2, 0)
        with self.assertRaises(ValueError):
            r.update(1, 2, 3, -1)
        with self.assertRaises(ValueError):
            r.update(1, 2, 3, 4, -1)

    def test_update_kwargs(self):
        r = Rectangle(4, 2, 1, 0, 65)
        r.update(id=98)
        self.assertEqual(r.__str__(), '[Rectangle] (98) 1/0 - 4/2')
        r.update(x=4)
        self.assertEqual(r.__str__(), '[Rectangle] (98) 4/0 - 4/2')
        r.update(height=3, y=1)
        self.assertEqual(r.__str__(), '[Rectangle] (98) 4/1 - 4/3')
        r.update(x=0, width=2, y=1)
        self.assertEqual(r.__str__(), '[Rectangle] (98) 0/1 - 2/3')
        r.update(width=2, height=2, x=2, y=2)
        self.assertEqual(r.__str__(), '[Rectangle] (98) 2/2 - 2/2')

    def test_update_kwargs_exc(self):
        r = Rectangle(4, 4, 4, 4, 5)
        r.update(1, y=None)
        self.assertEqual(r.__str__(), '[Rectangle] (1) 4/4 - 4/4')
        r.update(1, 2, x=False, id=99) 
        self.assertEqual(r.__str__(), '[Rectangle] (1) 4/4 - 2/4')
        r.update(1, 2, 3, width=3.5, y=0, x=0)
        self.assertEqual(r.__str__(), '[Rectangle] (1) 4/4 - 2/3')
        r.update(1, 2, 3, 4, height=[])
        self.assertEqual(r.__str__(), '[Rectangle] (1) 4/4 - 2/3')
        r.update(1, 2, 6, x=-2)
        self.assertEqual(r.__str__(), '[Rectangle] (1) 4/4 - 2/6')
        r.update(1, 4, height=0)
        self.assertEqual(r.__str__(), '[Rectangle] (1) 4/4 - 4/6')
        r.update(1, 3, 3, 4, 5, y=-1)
        self.assertEqual(r.__str__(), '[Rectangle] (1) 4/5 - 3/3')
        r.update(1, 2, 3, 4, x=-1, y=-2, width=3, height=0)
        self.assertEqual(r.__str__(), '[Rectangle] (1) 4/5 - 2/3')

    def test_update_key_exc(self):
        r = Rectangle(4, 4, 4, 4, 5)
        r.update(height=1, breadth=0)
        self.assertEqual(r.__str__(), '[Rectangle] (5) 4/4 - 4/1')
        self.assertTrue(hasattr(r, 'breadth'))



if __name__ == '__main__':
    ut.main()
