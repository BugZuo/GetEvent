#!/usr/bin/bash python
# -*- coding=utf8 -*-

__author__ = 'zuozuo'


import pymongo


class DBConn:
    conn = None
    # servers = "mongodb://10.1.4.10:27017"
    # servers = "mongodb://localhost:27017"

    def connect(self):
        self.conn = pymongo.Connection(self.servers)

    def close(self):
        return self.conn.disconnect()

    def getConn(self):
        return self.conn

