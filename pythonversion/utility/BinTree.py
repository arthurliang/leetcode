'''
Created on Nov 16, 2014

@author: Arthur
'''
from Queue import Queue
import re

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class BinTree:
    def __init__(self):
        self.rootnode = None

    def DeserializationOnOJ(self, srlztnOnOJ):
        if srlztnOnOJ == "{}":
            return True

        paraValid = (srlztnOnOJ.startswith("{") and srlztnOnOJ.endswith("}"))
        if not paraValid:
            return False

        if re.search(r"#}\Z", srlztnOnOJ):
            return False

        datalist = srlztnOnOJ[1:-1].split(',')

        self.rootnode = TreeNode(None)
        tempq = Queue()
        tempq.put(self.rootnode)

        for index in range(len(datalist)):
            if tempq.empty():
                break
            treenode = tempq.get()
            if datalist[index] != '#':
                treenode.val = int(datalist[index])
                treenode.left = TreeNode(None)
                treenode.right = TreeNode(None)
                tempq.put(treenode.left)
                tempq.put(treenode.right)

        # TODO: is it possible to improve the whole function's performance
        self.deleteNonValidRootNode(self.rootnode)
        return True

    def deleteNonValidRootNode(self, rootnode):
        if rootnode == None:
            return
        if rootnode.left and rootnode.left.val == None:
            rootnode.left = None
        if rootnode.right and rootnode.right.val == None:
            rootnode.right = None
        self.deleteNonValidRootNode(rootnode.left)
        self.deleteNonValidRootNode(rootnode.right)

    def SerializationOnOJ(self):
        if self.rootnode == None:
            return "{}"

        srlztnOnOJ = "{"
        tempq = Queue()
        tempq.put(self.rootnode)

        while not tempq.empty():
            treenode = tempq.get()
            if treenode:
                srlztnOnOJ += str(treenode.val)
                tempq.put(treenode.left)
                tempq.put(treenode.right)
            else:
                srlztnOnOJ += '#'
            srlztnOnOJ += ','

        # TODO: is it possible to improve the whole function's performance
        result = re.sub(r"(,#)*,?\Z", r"", srlztnOnOJ)
        return result + '}'



    def SerializationOnOJ4BTnextProperty(self):
        if self.rootnode == None:
            return "{}"

        srlztnOnOJ = "{"
        cq = [self.rootnode]
        nq = []

        while cq:
            treenode = cq.pop(0)

            if treenode.left:
                nq.append(treenode.left)

            if treenode.right:
                nq.append(treenode.right)

            while treenode:
                srlztnOnOJ += str(treenode.val) + ','
                treenode = treenode.next
                if cq and cq[0] is treenode:
                    cq.pop(0)

            if not cq:
                srlztnOnOJ += '#' + ','
                t = cq
                cq = nq
                nq = t

        # TODO: is it possible to improve the whole function's performance
        result = re.sub(r",?\Z", r"", srlztnOnOJ)
        return result + '}'
