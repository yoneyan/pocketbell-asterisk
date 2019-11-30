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
        dic = {11: "あ", 12: "い", 13: "う", 14: "え", 15: "お"
            , 21: "か", 22: "き", 23: "く", 24: "け", 25: "こ"
            , 31: "さ", 32: "し", 33: "す", 34: "せ", 35: "そ"
            , 41: "た", 42: "ち", 43: "つ", 44: "て", 45: "と"
            , 51: "な", 52: "に", 53: "ぬ", 54: "ね", 55: "の"
            , 61: "は", 62: "ひ", 63: "ふ", 64: "へ", 65: "ほ"
            , 71: "ま", 72: "み", 73: "む", 74: "め", 75: "も"
            , 81: "や", 82: "（", 83: "ゆ", 84: "）", 85: "よ"
            , 91: "ら", 92: "り", 93: "る", 94: "れ", 95: "ろ"
            , 01: "わ", 02: "を", 03: "ん", 04: "゛", 05: "゜"
            , 16: "a", 17: "b", 18: "c", 19: "d", 10: "e"
            , 26: "f", 27: "g", 28: "h", 29: "i", 20: "j"
            , 36: "k", 37: "l", 38: "m", 39: "n", 30: "o"
            , 46: "p", 47: "q", 48: "r", 49: "s", 40: "t"
            , 56: "u", 57: "v", 58: "w", 59: "x", 50: "y"
            , 66: "z", 67: "?", 68: "!", 69: "-", 60: "/"
            , 76: "\\", 77: "&", 78: "", 79: "-", 70: ""
            , 86: "*", 87: "#", 88: " ", 89: "", 80: ""
            , 96: "1", 97: "2", 98: "3", 99: "4", 90: "5"
            , 06: "6", 07: "7", 08: "8", 09: "9", 00: "0" }






"""
    elif result[-2] == "#" and result[-1] == "#":
        agi.verbose("Finish")
        agi.hangup()
        sys.exit()
"""
