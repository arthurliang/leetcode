# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True

        if self.isBalanced(root.left) and self.isBalanced(root.right) \
           and abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1:
            return True

        return False

    def maxDepth(self, root):
        if root is None:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return max(leftDepth, rightDepth) + 1