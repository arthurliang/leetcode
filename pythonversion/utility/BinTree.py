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
        self.deleteNonValidTreeNode(self.rootnode)
        return True

    def deleteNonValidTreeNode(self, rootnode):
        if rootnode == None:
            return
        if rootnode.left and rootnode.left.val == None:
            rootnode.left = None
        if rootnode.right and rootnode.right.val == None:
            rootnode.right = None
        self.deleteNonValidTreeNode(rootnode.left)
        self.deleteNonValidTreeNode(rootnode.right)

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



    def SerializationOnOJbyPara(self, root):
        self.rootnode = root
        return self.SerializationOnOJ()



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


class BinSearchTree(BinTree):
    def __init__(self):
        pass

    # @param valuelist: a list
    # @return a root node of BST
    def generateBST(self, valuelist):
        root = None
        for i in range(len(valuelist)):
            root = self.insertValToBST(root, valuelist[i])
        return root

    # @param val: need insert
    # @return a root node of BST
    def insertValToBST(self, root, val):
        if root is None:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self.insertValToBST(root.left, val)
        elif val > root.val:
            root.right = self.insertValToBST(root.right, val)
        return root

    # @param val: need searched
    # @return a TreeNode which found
    def searchBST(self, root, val):
        if not root:
            return None
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return root


