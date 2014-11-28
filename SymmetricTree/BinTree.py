'''
Created on Nov 16, 2014

@author: Arthur
'''
import queue
import re

class TreeNode:
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

class BinTree:
    def __init__(self):
        self.rootnode = None

    def DeserializationOnOJ(self, srlztnOnOJ):
        paraValid = (srlztnOnOJ.startswith("{") and srlztnOnOJ.endswith("}"))
        if not paraValid:
            return False

        datalist = srlztnOnOJ[1:-1].split(',')

        self.rootnode = TreeNode()
        tempq = queue.Queue()
        tempq.put(self.rootnode)

        for index in range(len(datalist)):
            if tempq.empty():
                break
            treenode = tempq.get()
            if datalist[index] != '#':
                treenode.val = datalist[index]
                treenode.left = TreeNode()
                treenode.right = TreeNode()
                tempq.put(treenode.left)
                tempq.put(treenode.right)

        return True

    def SerializationOnOJ(self):
        srlztnOnOJ = "{"

        tempq = queue.Queue()
        tempq.put(self.rootnode)

        while not tempq.empty():
            treenode = tempq.get()
            if treenode.val != None:
                srlztnOnOJ += treenode.val
                tempq.put(treenode.left)
                tempq.put(treenode.right)
            else:
                srlztnOnOJ += '#'
            if tempq.empty():
                break
            srlztnOnOJ += ','

        result = re.sub(r"(,#)+\Z", r"", srlztnOnOJ)
        return result + '}'
