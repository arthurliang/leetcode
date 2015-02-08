# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# click to show hints.
#
# Hints:
# If you notice carefully in the flattened tree, each node's right child points
# to the next node of a pre-order traversal.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left is None:
            return

        t = root.left
        while t.right is not None:
            t = t.right
        t.right = root.right
        root.right = root.left
        root.left = None
