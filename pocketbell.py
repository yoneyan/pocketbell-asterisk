#!/usr/bin/env python
import sys
from asterisk.agi import *

list = []

agi = AGI()
agi.verbose("Started")
callerId = agi.env['agi_callerid']
agi.verbose("Call from %s" % callerId)



while True:
#  agi.stream_file('vm-extension')
  result = agi.wait_for_digit(-1)
  agi.verbose("got digit %s" % result)
  list.append(result)
  agi.verbose(list)
  if result.isdigit():
    agi.say_number(result)
  elif result == "\#":
      agi.verbose("Finish")
      agi.hangup()
      sys.exit()
'''
  else
   agi.verbose("bye!")
   agi.hangup()
   sys.exit()
'''
