#!/usr/bin/bash python
# -*- coding=utf8 -*-
__author__ = 'zuozuo'

import urllib
import json
import time
import random
import traceback
import sys
import os
import pdb
from collections import OrderedDict

def getContent(url):
    # second = random.uniform(4, 8)
    # second = 1
    # time.sleep(second)
    page = urllib.urlopen(url)
    data = page.read()
    return data

# content = getContent("http://192.168.172.44:7199/event/1/blogs/masn/1/24/?tags=&order=new&_type=&_=1435627886095")
# print content, u'这种活动没有分享', unicode(content, 'utf8') == u'这种活动没有分享'

def dealJsonURL():
    record = 0
    # error = False
    for x in range(118, 122):
        # if x == 69:
        #     break
        # if error:
        #     # x -= 1
        #     # os.remove('./second/%d.txt' % x)
        #     error = False
        #     break

        i = 1
        tag = True
        # time.sleep(2)
        print 'next page %d *********************************************************' % x
        while (tag):
            # if i == 20000:
            #     break
            url = "http://192.168.172.44:7199/event/%d/blogs/masn/%d/24/?tags=&order=new&_type=&_=1435627886095" % (x, i)
            content = getContent(url)

            # 如果返回api为没有分享,则继续下一个活动探索
            if unicode(content, 'utf8') == u'这种活动没有分享':
                print '这种活动没有分享'
                break

            try:
                jsonContent = json.loads(content, encoding="utf8")
                if jsonContent['data']:
                    if 'blogs' in jsonContent['data'].keys():
                        items = jsonContent['data']['blogs']
                        with open('./second/%d.txt' % x, 'a') as f:
                            for j in range(0,len(items)):
                                blog = items[j]
                                id = blog['id']
                                if not id:
                                    break
                                # print i, id
                                f.write(str(id) + "\n")
                                record += 1
                    elif 'albums' in jsonContent['data'].keys():
                        items = jsonContent['data']['albums']
                        with open('./second/event_%d_album.txt' % x, 'a') as f:
                            for j in range(0, len(items)):
                                album = items[j]
                                id = album['id']
                                if not id:
                                    break
                                f.write(str(id) + "\n")
                                record += 1
                    else:
                        tag = False
                        print 'no album', x, i
                        break
                else:
                    break
                if not items:
                    tag = False
                    break
                print i
                i += 1
            except:  # 一旦页面打开失败, 页面不变,继续加载,直到加载完全,该异常不会让程序停止
                exc = "".join(traceback.format_exception(*sys.exc_info()))
                print exc, '活动%d, 页数%d' % (x, i)
                # error = True
                # break
    print record, i, 'over'

if __name__ == '__main__':
    dealJsonURL()
