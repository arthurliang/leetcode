# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
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
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        rslt = []
        curLevel = []
        cq = [root]
        nq = []
        reverse = True
        while len(cq) != 0:
            node = cq.pop()
            curLevel.append(node.val)

            if reverse:
                if node.left is not None:
                    nq.append(node.left)
                if node.right is not None:
                    nq.append(node.right)
            else:
                if node.right is not None:
                    nq.append(node.right)
                if node.left is not None:
                    nq.append(node.left)

            if len(cq) == 0:
                reverse = not reverse
                t = cq
                cq = nq
                nq = t
                rslt.append(curLevel)
                curLevel = []

        return rslt
