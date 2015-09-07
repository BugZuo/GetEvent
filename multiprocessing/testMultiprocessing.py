# coding=utf-8
__author__ = 'zuozuo'

import os
import json

print ('Process (%s) start...') % os.getpid()

s = '你好'

print json.dumps(s.decode('utf-8'))
print json.dumps(s)