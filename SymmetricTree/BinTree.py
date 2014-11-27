'''
Created on Nov 16, 2014

@author: Arthur
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinTree:
    def __init__(self):
        self.rootnode = None
        pass

    def DeserializationOnOJ(self, srlztnOnOJ):
        paraValid = (srlztnOnOJ.startswith("{") and srlztnOnOJ.endswith("}"))
        if not paraValid:
            return False
        if srlztnOnOJ == "{#}":
            return
        self.rootnode = TreeNode(1)
        pass

    def SerializationOnOJ(self, rootnode):
        pass