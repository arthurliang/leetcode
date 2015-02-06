# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Queue import Queue

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

                rst.append(curLevelRst)
                curLevelRst = []

        return rst
