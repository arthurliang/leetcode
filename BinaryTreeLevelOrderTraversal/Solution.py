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
        tempQueue = Queue()
        tempQueue.put(root)

        tempLevelList, tempQueue = self.getLevelList(tempQueue)
        while tempLevelList != None:
            rst.append(tempLevelList)
            tempLevelList, tempQueue = self.getLevelList(tempQueue)

        return rst

    def getLevelList(self, curlevelqueue):
        if curlevelqueue.empty():
            return None, None

        levelvalrst = []
        nextlevelqueue = Queue()
        while not curlevelqueue.empty():
            temptn = curlevelqueue.get()
            if temptn.left is not None:
                nextlevelqueue.put(temptn.left)
            if temptn.right is not None:
                nextlevelqueue.put(temptn.right)
            levelvalrst.append(temptn.val)

        return levelvalrst, nextlevelqueue

