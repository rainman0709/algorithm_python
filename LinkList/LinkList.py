#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node(object):
    '''
    data: 节点保存的数据
    _next: 保存下一个节点对象
    '''
    def __init__(self,data,pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        '''
        用来定义None的字符输出
        print为输出data
        '''
        return str(self.data)

class SingleList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def inEmpty(self):
        pass

    def append(self,dataOrNode):
        pass

    def delete(self,index):
        pass

    def insert(self,index,dataOrNode):
        pass

    def update(self,index,data):
        pass

    def getItem(self,index):
        pass

    def getIndex(self,data):
        pass

    def clear(self):
        pass

    def __repr__(self):
        pass

    def __getitem__(self, ind):
        pass

    def __setitem__(self, ind, value):
        pass

    def __len__(self):
        return self.length