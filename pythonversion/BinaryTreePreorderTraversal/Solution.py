# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        # solution recursive, just for try
        rslt = []
        if root is None:
            return rslt

        rslt.append(root.val)

        rslt.extend(self.preorderTraversal(root.left))

        rslt.extend(self.preorderTraversal(root.right))

        return rslt