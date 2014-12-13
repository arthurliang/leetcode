# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None:
            return []

        rst = []
        curLevelRst = []

        curLevelQueue = Queue()
        nextLevelQueue = Queue()

        curLevelQueue.put(root)
        while not curLevelQueue.empty():
            treenode = curLevelQueue.get()
            curLevelRst.append(treenode.val)
            if treenode.left is not None:
                nextLevelQueue.put(treenode.left)
            if treenode.right is not None:
                nextLevelQueue.put(treenode.right)

            if curLevelQueue.empty():
                temp = curLevelQueue
                curLevelQueue = nextLevelQueue
                nextLevelQueue = temp

                rst.insert(0, curLevelRst)
                curLevelRst = []

        return rst