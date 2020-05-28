
registry = {}

class Mulitimethod(object):
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
def multimethod(num): #name parameter
    def register(function):
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = Mulitimethod(name)
        mm.register(num, function)
        return mm
    return register