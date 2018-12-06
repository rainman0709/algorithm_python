#!/usr/bin/python
# -*- coding: utf-8 -*-




class Stack(object):
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def push(self, data):
        if self.isfull():
            raise Exception('the stack is full!')
        else:
            self.stack.append(data)
            self.top += 1

    def pop(self, data):
        if self.isempty():
            raise Exception('the stack is empty!')
        else:
            self.stack.pop(data)
            self.top -= 1

    def isfull(self):
        #return len(self.stack) == self.size
        return self.top + 1 == self.size

    def isempty(self):
        return self.top == -1

    def showStack(self):
        print(self.stack)