registry={}
class Mulitimethod(object):
    def __init__(self,name):
        self.name=name
        self.typemap={}
    def __call__(self, *args, **kwargs):
        num=len(args)
        function=self.typemap.get(num)
        if function is None:
            raise TypeError("no match")
        return function(*args)
    def register(self,types,function):
        if types in self.typemap:
            raise TypeError("duplicate redisteration")
        self.typemap[types] = function

def multimethod(num): #position parameter
    def register(function):
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = Mulitimethod(name)
        mm.register(num, function)
        return mm
    return register


















