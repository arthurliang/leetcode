# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBSTExt(root)[0]

    # @param root: a tree node0
    # @ return a tuple which include 3 elements: boolean, min value in tree, max value in tree
    def isValidBSTExt(self, root):
        if root is None:
            return (True, None, None)

        if root.left is None and root.right is None:
            return (True, root.val, root.val)

        rsltleft = self.isValidBSTExt(root.left)
        if not rsltleft[0]:
            return rsltleft
        rsltright = self.isValidBSTExt(root.right)
        if not rsltright[0]:
            return rsltright

        if rsltleft[2] < root.val and (root.right is None or root.val < rsltright[1]):
            curMinVal = root.val if root.left is None else rsltleft[1]
            curMaxVal = root.val if root.right is None else rsltright[2]
            return (True, curMinVal, curMaxVal)
        else:
            return (False, None, None)


