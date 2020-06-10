import unittest
from er import multimethod
from er import multimethods
from er import multimethod1
from er import multimethod2
from inherit2 import *
from mulinheritances import *
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
                return a+b
        Y=B()
        self.assertEqual(Y.foo(1),11)
    def test_multimethod1(self):

        @multimethod1(2)
        def foo(a, b):
            return a+b

        @multimethod1(3)
        def foo( a,b,c):
            return a+b+c

        @multimethod1(4)
        def foo(a, b, c,d):
            return a + b + c+d


        self.assertEqual(foo(1,2),3)
        self.assertEqual(foo(1,1,2,1),5)



    def test_multimethod2(self):
        @multimethod2(3)
        def foo(a, b,d):
            return a+b+d
        self.assertEqual(foo(1,2,d=1),4)
        @multimethod2(4)
        def foo(a,b,c,d):
            return a+b+c+d
        self.assertEqual(foo(1,2,c=3,d=1),7)

    def test_inherit(self):
        self.assertEqual(cx_A(2,3),cx_B(2,3))

    def test_mulinheritance(self):
        @multimethodM(A, B)
        def foo(a, b):
            return 'BB'

        @multimethodM(A, A)
        def foo(a, b):
            return 'do'

        self.assertEqual(foo(A(), B()), 'BB')
        self.assertEqual(foo(A(), A()), 'do')





if __name__ == '__main__':
    unittest.main()