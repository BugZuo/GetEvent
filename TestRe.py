#!/usr/bin/env python
# -*- coding:utf8 -*-
__author__ = 'zuozuo'

import MongoDBConn
import re
import json
import datetime
import os
from mysql import connector
from collections import OrderedDict


dbconn = MongoDBConn.DBConn()
conn = None
quality_album = None
def process():
    dbconn.connect()
    global conn
    conn = dbconn.getConn()

    quality_album = conn.albumDB.quality_album

    kw = '艺术'
    reg = re.compile(kw)
    params = {
        "$or": [
            {'name': kw},
            {'tags': kw},
            {'desc': kw},
        ]
    }
    rows = quality_album.find(params).limit(10)
    print_result(rows)


def print_result(rows):
    for row in rows:
        for key in row.keys():  # 遍历字典
            print key, row[key]  # 加,不换行打印


if __name__ == '__main__':
    # process()
    # test = '{"groups":[{"group_name":"首焦","ad_ids":["IGA001","ISA001","ANA001","IAR001","ABI001"]},{"group_name":"流行趋势","ad_ids": ["IGA004","ANA004"]},{"group_name": "不常用位置","ad_ids": ["IGA005","IAR002","IKA001","IKA002","IKA003","IKA004","IKA005","IFR001","ISAU01","ABI002","AAN001","AJA001"]},{"group_name": "blog_banner","ad_ids":["IGA005"]},{"group_name": "search_banner","ad_ids":["IGA006"]},{"group_name": "开屏","ad_ids":["IGA007"]}]}'
    # test2 = '[{"group_name":"首焦","ad_ids":["IGA001","ISA001","ANA001","IAR001","ABI001"]},{"group_name":"流行趋势","ad_ids": ["IGA004","ANA004"]},{"group_name": "不常用位置","ad_ids": ["IGA005","IAR002","IKA001","IKA002","IKA003","IKA004","IKA005","IFR001","ISAU01","ABI002","AAN001","AJA001"]},{"group_name": "blog_banner","ad_ids":["IGA005"]},{"group_name": "search_banner","ad_ids":["IGA006"]},{"group_name": "开屏","ad_ids":["IGA007"]}]'
    #
    # j = json.loads(test)
    # for group in j.get('groups'):
    #     if group['group_name'] == u'首焦':
    #         for ad_id in group['ad_ids']:
    #             print ad_id,

    # configs = '[ {"ad_id": "IGA001","alias": "iOS 首焦","group": "首焦"},{"ad_id": "ANA001","alias": "Android 首焦","group": "首焦"}]'
    # content = {
    #     "ad_id": "IGA001",
    #     "alias": "iOS 首焦",
    #     "group": "首焦",
    # }
    # j = json.dumps(content)
    # l = json.dumps(j)
    # L = dict([(x["ad_id"], x) for x in j])
    # print L
    # print type(j)
    # cnx = connector.connect(user='root', password='asd', host='localhost', database='test')
    # cur = cnx.cursor()
    # cur.execute('select * from test')
    # print cur.fetchall()
    # cnx.close()
    active_device_map = [
        ('1_week', '一周活跃用户'),  # 7天内
        ('1_2_week', '一周前活跃用户'),  # 7-14天
        ('2_3_week', '两周前活跃用户'),  # 14-21天
        ('3_4_week', '三周前活跃用户'),  # 21-28天
        ('4_8_week', '浅度沉默用户'),  # (4周-8周) 28-56天
        ('8_10_week', '中度沉默用户'),  # (8-10周) 56-60天
        ('10_week', '深度沉默用户')  # (10周前) 大于60天
    ]

    # L = sorted(active_device_map.items(), key=lambda item: int(item[0].split('_')[0]))
    dic = OrderedDict(active_device_map)
    for k, v in dic.items():
        print k, ':', v
