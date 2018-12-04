#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, val, pnext=None):
        self.data = val
        self.next = pnext


class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):
        if self.is_empty():
            print('LinkList is empty!')
            return
        elif key < 0 or key > self.getlength():
            print('the key is error!')
            return
        else:
            self.getitem(key)

    def __setitem__(self, key, value):
        if self.getlength() == 0:
            print('LinkList is empty!')
            return
        elif key < 0 or key > self.getlength():
            print('the key is error!')
            return
        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self, data):
        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):
        p = self.head
        length = 0
        while p is not None:
            length += 1
            p = p.next

        return length

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    def clear(self):
        self.head = 0

    def append(self, item):
        node = Node(item)
        if not self.head:
            self.head = node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = node

    def getitem(self, index):
        pass

    def insert(self):
        pass

    def delete(self, index):
        if self.is_empty():
            print('LinkList is empty!')
            return

        if index < 0 or index > self.getlength():
            pass

    def index(self):
        pass
