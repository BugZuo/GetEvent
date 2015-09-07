#!/usr/bin/bash python
# -*- coding:utf8 -*-

__author__ = 'zuozuo'


import MongoDBConn
import time

dbconn = MongoDBConn.DBConn()
conn = None
topics_event = None

def process():
    # 建立连接
    dbconn.connect()
    global conn
    conn = dbconn.getConn()

    print conn.server_info()

    databases =conn.database_names()
    print databases

    # dropTable()
    # 创建数据库

    # createTable()

    # 清空表
    emptyTable()

    # 插入数据
    insertData()

    # 打开指定表
    # openTable()
    
    # 查询插入的数据
    # queryData()

    dbconn.close()


def createTable():
    global topics_event
    topics_event = conn.topics.titan_event_archive

def openTable():
    global topics_event
    topics_event = conn.topics.titan_event_archive

def insertData():
    L = []
    # x = '2'
    for x in range(2, 122):
        try:
            datas = []
            with open('./second/%d.txt' % x, 'r') as f:
                for line in f.readlines():
                    data = {'id': x, 'blogid': int(line.strip())}
                    datas.append(data)
            topics_event.insert(datas)

            time.sleep(2)
        except:
            print 'no file'
            continue
        # if x == 2:
        #     break


def queryData():
    rows = topics_event.find({'id': 2}).limit(24).skip(0)
    print type(rows), rows
    blogids = []
    for row in rows:
        blogids.append(row['blogid'])

    print blogids
    # printResult(rows)


def dropTable():
    global conn
    conn.drop_database("topics")


def emptyTable():
    global topics_event
    topics_event = conn.topics.titan_event_archive
    topics_event.remove()


def printResult(rows):
    for row in rows:
        for key in row.keys():  # 遍历字典
            print row[key],  # 加,不换行打印


if __name__ == '__main__':
    process()
    # queryData()