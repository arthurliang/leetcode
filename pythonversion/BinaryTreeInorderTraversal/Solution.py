# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
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
    def inorderTraversal(self, root):
        # solution recursive, just for try
        rslt = []
        if root is None:
            return rslt

        rslt.extend(self.inorderTraversal(root.left))

        rslt.append(root.val)

        rslt.extend(self.inorderTraversal(root.right))

        return rslt