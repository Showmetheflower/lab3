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


registry1={}
class Mulitimethod1(object):
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

def multimethod1(num): #optional parameter
    def register(function):
        name = function.__name__
        mm = registry1.get(name)
        if mm is None:
            mm = registry1[name] = Mulitimethod1(name)
        mm.register(num, function)
        return mm
    return register


registry2 = {}

class Mulitimethod2(object):
    def __init__(self, name):
        self.name = name
        self.typemap = {}

    def __call__(self, *args, **kwargs):
        num = len(args)
        num2 = num + len(kwargs)
        if (num > 2):
            raise TypeError("illegal")
        else:
            function = self.typemap.get(num2)
            if function is None:
                raise TypeError("no match")
            return function(*args, **kwargs)

    def register(self, types, function):
        if types in self.typemap:
            raise TypeError("duplicate redisteration")
        self.typemap[types] = function
def multimethod2(num): #name parameter
    def register(function):
        name = function.__name__
        mm = registry2.get(name)
        if mm is None:
            mm = registry2[name] = Mulitimethod2(name)
        mm.register(num, function)
        return mm
    return register






    
















