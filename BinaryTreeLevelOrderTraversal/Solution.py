# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):

        # TODO: need to know what should be return (None or []) when root is None
        rst = []

        tq = queue.Queue()
        tq.put(root)

        tempLevelList, tq = self.getLevelList(tq)
        while tempLevelList != None:
            rst.append(tempLevelList)
            tempLevelList, tq = self.getLevelList(tq)

        return rst

    def getLevelList(self, curlevelqueue):
        if curlevelqueue.empty():
            return None, None

        levelvalrst = []
        nextlevelqueue = queue.Queue()
        while not curlevelqueue.empty():
            temptn = curlevelqueue.get()
            if temptn == None:
                return None, None
            if temptn.left != None:
                nextlevelqueue.put(temptn.left)
            if temptn.right != None:
                nextlevelqueue.put(temptn.right)
            levelvalrst.append(temptn.val)

        return levelvalrst, nextlevelqueue

