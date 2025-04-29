def mydecorator(cls):
    old_method = cls.__init__
    def _mydecorator(self,*args,**kwargs):
        print(f'@mydecorator before {old_method.__name__}')
        if kwargs != {}:
            try:
                for val in kwargs.values():
                    if type(val) != int:
                       raise TypeError(f"Значення елементів словника об'єкту не є цільми числами")
            except ValueError as e:
                print(e)
        print(f'@mydecorator after {old_method.__name__}')
        return old_method(self,*args,**kwargs)
    cls.__init__ = _mydecorator
    return cls

@mydecorator
class MyClass:
    def __init__(self,*args,**kwargs):
        self.args = args
        self.kw = kwargs

    def __str__(self):
        return  str(self.kw)

    def med(self,c):
        return c

d = {'a':5, 'b':2}
a = MyClass(**d)
print(a)