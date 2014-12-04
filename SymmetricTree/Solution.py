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
        if root == None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, leftTreeNode, rightTreeNode):
        if leftTreeNode == None and rightTreeNode == None:
            return True

        if leftTreeNode == None or rightTreeNode == None:
            return False

        if leftTreeNode.val != rightTreeNode.val:
            return False

        if not self.isMirror(leftTreeNode.left, rightTreeNode.right):
            return False
        if not self.isMirror(leftTreeNode.right, rightTreeNode.left):
            return False
        return True