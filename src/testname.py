"""test for named arguments"""
import unittest
from name import multimethod


class NamedArgsTest(unittest.TestCase):
    def test_multimethod(self):
        @multimethod(2)
        def foo(a, b):
            return a+b
        self.assertEqual(foo(a=1, b=2), 3)

        @multimethod(3)
        def foo(a, b, d):
            return a+b+d
        self.assertEqual(foo(1, 2, d=1), 4)

        @multimethod(4)
        def foo(a, b, c, d):
            return a+b+c+d
        self.assertEqual(foo(1, 2, c=3, d=1), 7)


if __name__ == '__main__':
    unittest.main()



