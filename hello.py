#!/usr/bin/env python3

import common

class MyClass(object):
    def __init__(self, s):
        self.s = s

@common.checkargs
def say(word: MyClass):
    print("Hello, %s!" % word.s)

say(MyClass("Hello"))
say(MyClass(12))
say(MyClass("Another"))
