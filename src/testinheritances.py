
import unittest
from inheritances import multimethodB
class MultimethodTestCase(unittest.TestCase):
    def test_multimethod(self):
        class A(object):
            @multimethodB(int,int)
            def foo(a, b):
                return a+b

            @multimethodB(float, float)
            def foo( a, b):
                return "float, float"

            @multimethodB(str, str)
            def foo(a, b):
                return "str, str"

        X=A()
        #print(X.foo(1,2))
        self.assertEqual(X.foo(1,2),3)
        self.assertEqual(X.foo(1.2,1.3),'float, float')
        self.assertEqual(X.foo("1","2"),"str, str")

if __name__ == '__main__':
    unittest.main()