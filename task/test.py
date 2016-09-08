#coding=utf8
#添加操作模块
import os
import sys
from plugins.plugin_test import plugin_test

def task():
    test=plugin_test()
    print test.getinfo()
    test.printstr('print text for test')
