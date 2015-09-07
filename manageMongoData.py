#!/usr/bin/env python
# -*- coding:utf8 -*-

import MongoDBConn
import datetime
db = MongoDBConn.DBConn()
db.connect()
global conn
conn = db.getConn()


def process_tasks():
    push_db = conn['push_db']
    tasks_dao = push_db['tasks']
    cursor = tasks_dao.find()
    print 'Begin'
    i = 0
    for c in cursor:
        # print c
        app_codes = []
        if c.has_key('app_codes'):
            print '--------------------------', c['_id']
            print 'Done, total -->', i
            break
        i = i + 1
        # try:
        #     app_codes.append(c['app_code'])
        #     c.pop('app_code')
        # except:
        #     print '-------------------------------', c
        app_codes.append(c['app_code'])
        data = {
            "_id": c['_id'],
            "state": c['state'],
            "mtime": c['mtime'],
            "url": c['url'],
            "text": c['text'],
            "ctime": c['ctime'],
            "desc": c['desc'],
            "scheduled": c['scheduled'],
        }
        target = {}
        if c['target'] == 'ALL' or not c['target']:
            target = {
                "target": {
                    "type": "for_all",
                    "app_codes": app_codes,
                }
            }
            # process_target(data, target)
            c.update(target)
        elif c['target']:
            tokens = c['target'].split('\n')
            target = {
                "target": {
                    "type": "token",
                    "app_codes": app_codes,
                    "tokens": tokens,
                }
            }
            c.update(target)
        # print c
        # tasks_dao.save(c)
        process_target(data, target, i)
        tasks_dao.remove({"_id": c['_id']})
        tasks_dao.insert(data)


def process_target(data, target, i):
    data.update(target)
    print i, "data: ------->   ", data

# {
#         "_id" : ObjectId("555590e2ba260b4c54ac0ab8"),
#         "state" : "DONE",
#         "target" : "40a876dc6a54cc4c4796bf64e0c1bfe8f2ccdf6a",
#         "mtime" : 1431670000,
#         "url" : "http://www.duitang.com/guide/event/snackstillnow/?from=app&__urlopentype=pageweb&__dtac=%7B%22from_pushnotification%22%3A%201%7D",
#         "text" : "不好好吃饭，就知道吃零食！",
#         "app_code" : 2,
#         "ctime" : 1431670000,
#         "desc" : "android test",
#         "scheduled" : -1
# }


def process_banner():
    conn = db.getConn()
    bannerDB = conn['bannerDB']
    banner_dao = bannerDB['banner']

    result = banner_dao.find({"adIds":{"$in":["ANA006"]}}).limit(10)

    for r in result:
        print r, r.keys
        # data = {
        #     "fixedIndex": r['fixedIndex'] if r.has_key('fixedIndex') else "",
        #     "picture": r['picture'],
        #     "tag_title": r['tag_title'] if r.has_key('tag_title') else "",
        #     "target": r['target'],
        #     "adIds": ['ANA006'],
        #     "stitle": r['stitle'] if r.has_key('stitle') else "",
        #     "disableAt": r['disableAt'] if r.has_key('disableAt') else "",
        #     "targetId": r['targetId'],
        #     "indexDisableAt": r['indexDisableAt'] if r.has_key('indexDisableAt') else "",
        #     "indexEnableAt": datetime.datetime.now(),
        #     "tag": r['tag'] if r.has_key('tag') else "",
        #     "enableAt": r['enableAt'],
        #     "action": r['action'],
        #     "type": r['type'],
        #     "isEnabled": r['isEnabled'],
        #     "desc": r['desc'],
        #     "createAt": datetime.datetime.now(),
        # }
        # banner_dao.insert(data)
        # r['adIds'] = r['adIds'].remove('IGA007')
        r['isEnabled'] = True
        r['adIds'] = [u'ANA006', u'ANA007']
        banner_dao.save(r)

if __name__ == '__main__':
    process_tasks()
