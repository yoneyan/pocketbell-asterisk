#!/usr/bin/env python
import sys
import threading
#from flask import Flask
import time

from asterisk.agi import *

dial_first = []
dial = []
send = []


def dial_input():
    x = agi.wait_for_digit(-1)
    agi.verbose(x)
    return x

"""
def judgement():
    while True:
        if len(dial) % 2 == 0:
            send.append(dial.pop(0))
"""

agi = AGI()

agi.verbose("Started")
callerId = agi.env['agi_callerid']
agi.verbose("Call from %s" % callerId)

'''
while len(dial_first) != 4:
    result = dial_input()
    dial_first.append(result)
    agi.say_ntime.sleepumber(result)
    agi.verbose(dial_first)# if len(dial) != 0:
'''

#threading.Thread(target=judgement).start()

while True:
    result = dial_input()
    agi.verbose("got digit %s" % result)
    # if len(dial) != 0:
    dial.append(result)
    agi.verbose("dial: " + ("".join(dial)))
    agi.verbose("send: " + ("".join(send)))
    if result.isdigit():
        agi.say_number(result)
    if len(dial) % 2 == 0:
        text_first = dial[-2]
        text_second = dial[-1]
        agi.verbose("dial: " + ("".join(dial)))
        dic = {11: "あ", 12: "い", 13: "う", 14: "え", 15: "お"}






"""
    elif result[-2] == "#" and result[-1] == "#":
        agi.verbose("Finish")
        agi.hangup()
        sys.exit()
"""
