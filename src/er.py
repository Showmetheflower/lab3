registry={}

class Mulitimethod(object):
    def __init__(self,name):
        self.name=name
        self.typemap={}
    def __call__(self, *args, **kwargs):
        types=tuple(arg.__class__ for arg in args)
        function=self.typemap.get(types)
        if function is None:
            raise TypeError("no match")
        return function(*args)
    def register(self,types,function):
        if types in self.typemap:
            raise TypeError("duplicate redisteration")
        self.typemap[types] = function

def multimethod(*types): #position parameter
    def register(function):
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = Mulitimethod(name)
        mm.register(types, function)
        return mm
    return register
def multimethods(*types):  #Defaults parameter
    def register(function):
        function = getattr(function, "__lastreg__", function)
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm.registry[name]=Mulitimethod(name)
        mm.register(types, function)
        mm.__lastreg__ = function
        return mm
    return register


    
















