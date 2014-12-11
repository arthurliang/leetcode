# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        rst = []
        tempQueue = []
        tempQueue.append(root)

        tempLevelList, tempQueue = self.getLevelList(tempQueue)
        while tempLevelList != None:
            rst.append(tempLevelList)
            tempLevelList, tempQueue = self.getLevelList(tempQueue)

        return rst

    def getLevelList(self, curlevelqueue):
        if not curlevelqueue:
            return None, None

        levelvalrst = []
        nextlevelqueue = []
        while curlevelqueue:
            temptn = curlevelqueue.pop(0)
            if temptn == None:
                return None, None
            if temptn.left != None:
                nextlevelqueue.append(temptn.left)
            if temptn.right != None:
                nextlevelqueue.append(temptn.right)
            levelvalrst.append(temptn.val)

        return levelvalrst, nextlevelqueue

