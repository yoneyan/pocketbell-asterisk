#!/usr/bin/env python
import sys
#import threading
#from flask import Flask
from asterisk.agi import *

dial_first = []
dial = []
send = []


def dial_input():
    x = agi.wait_for_digit(-1)
    agi.verbose(x)
    return x


agi = AGI()

agi.verbose("Started")
callerId = agi.env['agi_callerid']
agi.verbose("Call from %s" % callerId)

while len(dial_first) != 4:
    result = dial_input()
    dial_first.append(result)
    agi.say_number(result)
    agi.verbose(dial_first)

    #    threading.Thread(target=judgment()).start()

while True:
    result = dial_input()
    agi.verbose("got digit %s" % result)
    # if len(dial) != 0:
    dial.append(result)
    agi.verbose(dial)
    if result.isdigit():
        agi.say_number(result)

"""
    elif result[-2] == "#" and result[-1] == "#":
        agi.verbose("Finish")
        agi.hangup()
        sys.exit()
"""
