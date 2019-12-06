#!/usr/bin/env python3
import time
import config

from asterisk.agi import *
from requests_oauthlib import OAuth1Session


dial_first = []
dial = []
data = []

agi = AGI()
agi.verbose("Started")
callerId = agi.env['agi_callerid']
agi.verbose("Call from %s" % callerId)

dic = {"11": "あ", "12": "い", "13": "う", "14": "え", "15": "お", "16": "a", "17": "b", "18": "c", "19": "d",
       "10": "e", "1*": "all_delete", "1#": "",
       "21": "か", "22": "き", "23": "く", "24": "け", "25": "こ", "26": "f", "27": "g", "28": "h", "29": "i",
       "20": "j", "2*": "all_delete", "2#": "",
       "31": "さ", "32": "し", "33": "す", "34": "せ", "35": "そ", "36": "k", "37": "l", "38": "m", "39": "n",
       "30": "o", "3*": "all_delete", "3#": "",
       "41": "た", "42": "ち", "43": "つ", "44": "て", "45": "と", "46": "p", "47": "q", "48": "r", "49": "s",
       "40": "t", "4*": "all_delete", "4#": "",
       "51": "な", "52": "に", "53": "ぬ", "54": "ね", "55": "の", "56": "u", "57": "v", "58": "w", "59": "x",
       "50": "y", "5*": "all_delete", "5#": "",
       "61": "は", "62": "ひ", "63": "ふ", "64": "へ", "65": "ほ", "66": "z", "67": "?", "68": "!", "69": "-",
       "60": "/", "6*": "all_delete", "6#": "",
       "71": "ま", "72": "み", "73": "む", "74": "め", "75": "も", "76": "=", "77": "&", "78": "@", "79": ".",
       "70": "_", "7*": "all_delete", "7#": "",
       "81": "や", "82": "（", "83": "ゆ", "84": "）", "85": "よ", "86": "*", "87": "#", "88": "space", "89": "",
       "80": "", "8*": "all_delete", "8#": "",
       "91": "ら", "92": "り", "93": "る", "94": "れ", "95": "ろ", "96": "1", "97": "2", "98": "3", "99": "4",
       "90": "5", "9*": "all_delete", "9#": "",
       "01": "わ", "02": "を", "03": "ん", "04": "゛", "05": "゜", "06": "6", "07": "7", "08": "8", "09": "9",
       "00": "0", "0*": "all_delete", "0#": "",
       "*1": "test", "*2": "", "*3": "", "*4": "", "*5": "", "*6": "", "*7": "", "*8": "", "*9": "", "*0": "",
       "**": "all_delete", "*#": "",
       "#1": "", "#2": "", "#3": "", "#4": "", "#5": "", "#6": "", "#7": "", "#8": "", "#9": "", "#0": "",
       "#*": "", "##": "finish"
       }


class function:

    @staticmethod
    def dial_input():
        x = agi.wait_for_digit(-1)
        agi.verbose(x)
        return x

    @staticmethod
    def twitter_post(text):
        CK = config.CONSUMER_KEY
        CS = config.CONSUMER_SECRET
        AT = config.ACCESS_TOKEN
        ATS = config.ACCESS_TOKEN_SECRET
        twitter = OAuth1Session(CK, CS, AT, ATS)
        url = "https://api.twitter.com/1.1/statuses/update.json"
        params = {"status": text}
        res = twitter.post(url, params=params)
        if res.status_code == 200:
            agi.verbose("Success.")
        else:
            agi.verbose("Failed. : %d" % res.status_code)
            time.sleep(2)

    @staticmethod
    def end():
        agi.verbose("Finish")
        agi.hangup()
        sys.exit()


def dial_start():
    f = function()
    for i in range(4):
        dial_first.append(f.dial_input())
    return "".join(dial_first)


def twitter_section():
    f = function()
    while True:
        result = f.dial_input()
        dial.append(result)
        agi.verbose("dial: " + ("".join(dial)))
        if len(dial) % 2 == 0:
            text_first = dial[-2]
            text_second = dial[-1]
            text = dic.get(text_first + text_second)
            agi.verbose("data: " + ("".join(data)))
            if not text:
                continue
            if text == "finish":
                f.twitter_post("".join(data))
                f.end()
                break
            elif text == "all_delete":
                agi.verbose("all_delete")
                agi.say_number(0)
                dial.clear()
                data.clear()
                continue
            elif text == "test":
                continue
            elif text == "space":
                data.append(" ")
                agi.verbose("data: " + ("".join(data)))
            else:
                data.append(text)
                agi.verbose("data: " + ("".join(data)))


answer = dial_start()
if answer == "*2*2":
    twitter_section()
else:
    function.end()
