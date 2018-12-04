#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, val, p=0):
        self.data = val
        self.next = p


class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def initlist(self,data):
        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):
        p = self.head
        length = 0
        while p != 0:
            length += 1
            p = p.next

        return length

    def is_empty(self):
        pass

    def clear(self):
        pass

    def append(self):
        pass

    def getitem(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass

    def index(self):
        pass