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
        # Morris Inorder
        rslt = []
        cur = root

        while cur:
            if cur.left is None:
                rslt.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    rslt.append(cur.val)
                    pre.right = None
                    cur = cur.right

        return rslt

#         # solution iteratively
#         rslt = []
#         if root is None:
#             return rslt
#
#         stack = [root]
#         visited = []
#
#         while stack:
#             node = stack.pop()
#
#             if node in visited:
#                 rslt.append(node.val)
#                 continue
#             visited.append(node)
#
#             if node.right is not None:
#                 stack.append(node.right)
#             stack.append(node)
#             if node.left is not None:
#                 stack.append(node.left)
#
#         return rslt

#         # solution recursive, just for try
#         rslt = []
#         if root is None:
#             return rslt
#
#         rslt.extend(self.inorderTraversal(root.left))
#
#         rslt.append(root.val)
#
#         rslt.extend(self.inorderTraversal(root.right))
#
#         return rslt