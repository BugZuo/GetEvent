__author__ = 'zuozuo'

import datetime
import time

tz = time.localtime(1435161600)
st = time.strftime('%Y-%m-%d %H:%M:%S', tz)
print st