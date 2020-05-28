"""test for positional arguments"""
import unittest
from er import multimethod
from er import multimethods

import er


class PositionalArgsTestCase(unittest.TestCase):

    def test_add(self):
        """test multimethod"""
        class A(object):
            @multimethod(int, int)
            def add(a, b):
                return 'int: a+b = {}'.format(a+b)

            @multimethod(float, float)
            def add(a, b):
                return 'float: a+b = {}'.format(a+b)

            @multimethod(str, str)
            def add(a, b):
                return 'string: a+b = {}'.format(a+b)
        X = A()
        self.assertEqual(X.add(1, 2), 'int: a+b = 3')
        self.assertEqual(X.add(1.2, 1.3), 'float: a+b = 2.5')
        self.assertEqual(X.add('1', '2'), 'string: a+b = 12')

    def test_divide(self):
        """test multimethod"""
        class A(object):
            @multimethod(int, int)
            def divide(a, b):
                return 'int: a/b = {}'.format(int(a/b))

            @multimethod(float, float)
            def divide(a, b):
                return 'float: a/b = {}'.format(a/b)
        X = A()
        self.assertEqual(X.divide(5, 2), 'int: a/b = 2')
        self.assertEqual(X.divide(5.0, 2.0), 'float: a/b = 2.5')


if __name__ == '__main__':
    unittest.main()
