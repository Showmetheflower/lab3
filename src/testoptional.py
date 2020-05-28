import unittest
from optional import multimethod


class test(unittest.TestCase):
    def test_multimethod(self):

        @multimethod(2)
        def foo(a, b):
            return a+b

        @multimethod(3)
        def foo( a,b,c):
            return a+b+c

        @multimethod(4)
        def foo(a, b, c,d):
            return a + b + c+d


        self.assertEqual(foo(1,2),3)
        self.assertEqual(foo(1,1,2,1),5)
if __name__ == '__main__':
    unittest.main()



