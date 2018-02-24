from functools import wraps
import types
import time

class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError("Already started")
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError("Not started")
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None
    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

def timefunc(fn, *args, **kwargs):
    def fncomposite(*args, **kwargs):
        timer = Timer()
        timer.start()
        rt = fn(*args, **kwargs)
        timer.stop()
        print("Executing %s took %s seconds." % (fn.__name__, timer.elapsed))
    return fncomposite

class Timed(type):
    def __new__(cls, name, bases, attr):
        for name, value in attr.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                attr[name] = timefunc(value)
        return super(Timed, cls).__new__(cls, name, bases, attr)

class Math(metaclass=Timed):
    @staticmethod
    def multiply(a,b):
        product = a * b
        print(product)
        return product

Math.multiply(5,6)

class Shouter(metaclass=Timed):
    def intro(self):
        print("I shout!")

s = Shouter()
s.intro()

def divide(a,b):
    result = a/b

div = timefunc(divide)
div(9.3)







class Final(type):
    def __new__(cls, name, bases, attr):
        type_arr = [type(x) for x in bases]
        for i in type_arr:
            if i is Final:
                raise RuntimeError("You cannot subclass a Final class")
        return super(Final, cls).__new__(cls, name, bases, attr)

class Cop(metaclass=Final):
    def exit(self):
        print("Exiting...")
        quit()

class FakeCop(Cop):
    def scam(self):
        print("This is a hold up!")

cop1 = Cop()
fakecop1 = FakeCop()

class Goat(metaclass=Final):
    location = "Goatland"

class BillyGoat(Goat):
    location = "Billyland"




def notify(fn, *args, **kwargs):

    def fncomposite(*args, **kwargs):
        print("running %s" %fn.__name__)
        rt = fn(*args, **kwargs)
        return rt
    return fncomposite

class Notifies(type):
    def __new__(cls, name, bases, attr):
       for name, value in attr.items():
           if type(value) is types.FunctionType or type(value) is types.MethodType:
               attr[name] = notify(value)
       return super(Notifies, cls).__new__(cls, name, bases, attr)

class Math(metaclass=Notifies):
    @staticmethod
    def multiply(a, b):
        product = a*b
        print(product)
        return product

# Math.multiply(5,6)

class Shouter(metaclass=Notifies):
    def intro(self):
        print("I shout!")

s = Shouter()
s.intro()
# def notifyfunc(fn):
#     """prints out the function name before executing it"""
#     @wraps(fn)
#     def composite(*args, **kwargs):
#         print("Executing '%s'" % fn.__name__)
#         rt = fn(*args, **kwargs)
#         return rt
#     return composite
#
# @notifyfunc
# def multiply(a,b):
#     product = a*b
#     return product
#
#
#
#
# class HelloMeta(type):
#
#     def hello(cls):
#         print("greetings from %s, a HelloMeta type class" % (type(cls())))
#
#     def __call__(self, *args, **kwargs):
#         cls = type.__call__(self, *args)
#         setattr(cls, "hello", self.hello)
#         return cls
#
# class TryHello(object, metaclass=HelloMeta):
#     def greet(self):
#         self.hello()
#
#
# greeter = TryHello()
# greeter.greet()
#
# day = "Sunday"
# print("The type of variable day is %s" % (type(day)))
#
#
