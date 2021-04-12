#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The module is logger-related, and there exist some functions
of log.
"""
import datetime
import sys

# log level, 0 only println, 1 add infoln, 2 add debugln, 3 add verboseln
# println is used to record the most basic information
# infoln is used to record the information of each step at runtime
# debugln is used to record information that developers are concerned about
# verboseln is used for the highest level of record information, including various variables
lvl = 0

def println(*args):
    pre = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    print(pre, *args)

def infoln(*args):
    if lvl:
        println(*args)

def debugln(*args):
    if lvl >= 2:
        pre = 'DEBUG'
        println(pre, *args)

def verboseln(*args):
    if lvl >= 3:
        println(*args)

def panicln(*args):
    println(*args)
    raise Exception(' '.join(str(e) for e in args))


def fatalln(*args):
    println(*args)
    println('exit status 1')
    sys.exit(1)

lvl = 2


