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
        if root is None:
            return True

        return self.isValidBSTExt(root)[0]

    # @param root: a tree node which must not be None
    # @ return a tuple which include 3 elements: boolean, min value in tree, max value in tree
    def isValidBSTExt(self, root):
        assert(root is not None)

        isValid = 0
        minVal = 1
        maxVal = 2

        if root.left is None and root.right is None:
            return (True, root.val, root.val)

        if root.right is None:
            rslt = self.isValidBSTExt(root.left)
            if not rslt[isValid]:
                return rslt
            if rslt[maxVal] > root.val:
                return (False, None, None)
            return (True, rslt[minVal], root.val)

        if root.left is None:
            rslt = self.isValidBSTExt(root.right)
            if root.val > rslt[minVal]:
                return (False, None, None)


