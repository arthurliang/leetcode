# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        # iterative solution
        if root is None:
            return []

        rslt = []
        stack = [(root, False, False)]

        while stack:
            node, leftVisited, rightVisited = stack.pop()
            if not leftVisited and not rightVisited:
                sum -= node.val

            if node.left is None and node.right is None and sum == 0:
                rslt.append([x[0].val for x in stack] + [node.val])
                sum += node.val
                continue

            if not leftVisited and node.left is not None:
                leftVisited = True
                stack.append((node, leftVisited, rightVisited))
                stack.append((node.left, False, False))
                continue

            if not rightVisited and node.right is not None:
                rightVisited = True
                stack.append((node, leftVisited, rightVisited))
                stack.append((node.right, False, False))
                continue

            sum += node.val

        return rslt

#         # recursive solution
#         self.rslt = []
#         curPath = []
#
#         self.isPathSumValidAndUpdateResult(root, curPath, sum)
#
#         return self.rslt
#
#     def isPathSumValidAndUpdateResult(self, root, curPath, sum):
#         if root is None:
#             return
#
#         curPath.append(root.val)
#         sum -= root.val
#
#         if root.left is None and root.right is None and sum == 0:
#             self.rslt.append(curPath)
#             return
#
#         curPath2 = copy.copy(curPath)
#         self.isPathSumValidAndUpdateResult(root.left, curPath, sum)
#         self.isPathSumValidAndUpdateResult(root.right, curPath2, sum)
