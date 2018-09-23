#-All games cut scenes and text related questions-#
from gamecon import AnimatedText
import sys
import os
import time

def WhatName(name):
    AskQ = ("What is your name young one? ")
    AnimatedText(message = AskQ, speed = .05)
    time.sleep(1)
    name = input("~] ")
WhatName(name = str())

print (WhatName)
input("")
