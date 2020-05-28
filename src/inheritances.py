from er import Mulitimethod

registry={}
class B(Mulitimethod):
    def nn(self):
        print("this is a class which inherent from Mulitimethod")

def multimethodB(*types): #position parameter
    def register(function):
        name = function.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = B(name)
        mm.register(types, function)
        return mm
    return register

