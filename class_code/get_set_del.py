#!/usr/bin/env python
#coding=utf-8

class Test():
    def __init__(self, uname, age):
        self.__uname = uname
        self__age = age

    @property
    def uname(self):
        return self.__uname

    @uname.setter
    def uname(self, val):
        if not isinstance(val, str):
            raise TypeError('必须是字符串')
        self.__uname = val

    @uname.deleter
    def uname(self):
        raise TypeError('can not delete uname')

t1 = Test('测试', 20)
print t1.uname

t1.uname = '张三'
print t1.uname

t1.uname = '李四'
print t1.uname

t1.uname = 111
print t1.uname

del t1.uname
