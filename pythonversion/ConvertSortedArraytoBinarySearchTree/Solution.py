# Given an array where elements are sorted in ascending order,
# convert it to a height balanced BST.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utility.BinTree import TreeNode

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if num is None or len(num) == 0:
            return None

        root = TreeNode(0)
        stack = [(root, 0, len(num) - 1)]

        while stack:
            node, start, end = stack.pop()
            mid = (start + end) / 2
            node.val = num[mid]
            if mid - 1 >= start:
                node.left = TreeNode(0)
                stack.append((node.left, start, mid - 1))
            if mid + 1 <= end:
                node.right = TreeNode(0)
                stack.append((node.right, mid + 1, end))

        return root

