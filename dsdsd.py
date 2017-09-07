#!usr/bin/python
#-*- coding:utf-8 -*-
import sys


'''
理解魔术方法被调用的含义，理解my_test()和_my_test()在调用时的差别，__call__是在实例被调用的时候被自动执行，还有test_1 = LyTest(lalal(), "开始", "连接" ,"失败")
为什么一开始lalal()就被执行
'''
class LyTest:
    def __init__(self, construct_func, hint=None, end_hint=None, excp_hint=None):
        self._func = construct_func
        self._ins = None
        self._hint = hint
        self._end_hint = end_hint
        self._excp_hint = excp_hint

    def __call__(self):
        if not self._ins is None:
            return self._ins
        print (self._hint)
        try:
            self._ins = self._func
        except Exception:
            pass
            # print (self._excp_hint0
            # sys.exit(-1)
        # print(self._end_hint)
        return self._ins

    def my_test(self):
        print ("this is a test")


def lalal():
    import pdb
    # pdb.set_trace()
    print ("lalallalalal")


if __name__ == "__main__":
    test_1 = LyTest(lalal(), "开始", "连接" ,"失败")
    test_1.my_test()
    test_1()