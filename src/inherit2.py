import functools
class A(object):
    def __init__(self,k="do"):
        self.k=k
    def __call__(self, func):
        @functools.wraps(func)
        def __de(*args,**kwargs):
            if self.k=="do":
                self.notify(func)
            return func(*args,**kwargs)
        return __de
    def notify(self,func):
         print("%s running" %func.__name__)
@A(k="do")
def cx_A(a,b):
    return a+b

class B(A):
    def __init__(self,sex='femal',*args,**kwargs):
        self.sex=sex
        super(B,self).__init__(*args,**kwargs)
    def notify(self,func):
        print("%s running" %func.__name__)
        print("%sex " % self.sex)
@B(k="do")
def cx_B(a,b):
    return a+b





