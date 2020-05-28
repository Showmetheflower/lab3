import unittest
from er import multimethod
from er import multimethods

import er
class MultimethodTestCase(unittest.TestCase):
    def test_multimethod(self):
        class A(object):
            @multimethod(int,int)
            def foo(a, b):
                return "int, int"

            @multimethod(float, float)
            def foo( a, b):
                return "float, float"

            @multimethod(str, str)
            def foo(a, b):
                return "str, str"

        X=A()
        self.assertEqual(X.foo(1,2),'int, int')
        self.assertEqual(X.foo(1.2,1.3),'float, float')
        self.assertEqual(X.foo("1","2"),"str, str")
    def test_multimethods(self):
        class B(object):
            @multimethods(int)
            def foo(a,b=10):
                return "int"
        Y=B()
        self.assertEqual(Y.foo(1),'int')



if __name__ == '__main__':
    unittest.main()