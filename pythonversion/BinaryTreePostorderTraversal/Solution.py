# Given a binary tree, return the postorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [3,2,1].
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
    def postorderTraversal(self, root):
        # solution iteratively
        rslt = []
        if root is None:
            return rslt

        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if visited:
                rslt.append(node.val)
            else:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))

        return rslt


#         # solution recursive, just for try
#         rslt = []
#         if root is None:
#             return rslt
#
#         rslt.extend(self.postorderTraversal(root.left))
#
#         rslt.extend(self.postorderTraversal(root.right))
#
#         rslt.append(root.val)
#
#         return rslt