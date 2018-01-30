####1、通过format()函数和字符串方法使得一个对象能支持自定义的格式化，为了自定义字符串的格式化，我们需要在类上面定义__format__()方法。例如：
_formats = {
    "ymd": "{d.year}-{d.month}-{d.day}",
    "mdy": "{d.month}/{d.day}/{d.year}",
    "dmy": "{d.day}/{d.month}/{d.year}"
}
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == "":
            code = "ymd"
        fmt = _formats[code]
        return fmt.format(d=self)

####2、想让你的对象支持上下文管理协议（with语句），需要实现__enter__()和__exit__()方法
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.address, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None

####3、程序要创建大量（可能上百万）的对象，导致占用很大的内存，使用__slot__

####4、大多数而言，应该让非公共名称以单下划线开头。但是，如果知道代码会设计到子类，并且有些内部属性应该在子类中隐藏起来，那么才考虑使用双下划线方案

####5、如果想给某个实例attribute增加除访问与修改之外的其他处理逻辑，比如类型检查或合法性验证，自定义某个属性的一种简单方法是将它定义为一个property，

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("can't delete attribute")
####6想要在子类中调用父类的某个已经被覆盖的方法，可以使用super()函数
class A:
    def spam(self):
        print("A.spam")

class B(A):
    def spam(self):
        print("B.spam")
        super().spam()




if __name__ == '__main__':
    d = Date(2012, 12, 21)
    # print(format(d))
    # print(format(d, "mdy"))
    # print("The date is {:ymd}".format(d))
    print(format(d, "%A,%B %d, %Y"))
