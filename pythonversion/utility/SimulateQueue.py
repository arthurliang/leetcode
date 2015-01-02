'''
Created on Dec 11, 2014

@author: Arthur
'''

class Queue:
    def __init__(self):
        self.container = []

    def put(self, obj):
        self.container.append(obj)

    def get(self):
        return self.container.pop(0)

    def empty(self):
        return not self.container
