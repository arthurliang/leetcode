# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, leftTreeNode, rightTreeNode):
        if leftTreeNode is None and rightTreeNode is None:
            return True

        if leftTreeNode is None or rightTreeNode is None:
            return False

        if leftTreeNode.val != rightTreeNode.val:
            return False

        if not self.isMirror(leftTreeNode.left, rightTreeNode.right):
            return False
        if not self.isMirror(leftTreeNode.right, rightTreeNode.left):
            return False
        return True
