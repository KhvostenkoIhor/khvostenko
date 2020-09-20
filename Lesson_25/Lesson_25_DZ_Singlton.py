class Sing(object):
    __instance = None
    def __new__(cls, *val):
        if Sing.__instance is None:
            Sing.__instance = object.__new__(cls)
        Sing.__instance.val = val
        return Sing.__instance

a = Sing()
b = Sing()
print(a == b)

class SingDecor:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None
    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance

@SingDecor
class A():
	pass
	
a = A()
b = A()
print(a == b)
