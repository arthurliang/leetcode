# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False

        sum = sum - root.val
        if sum is 0 and root.left is None and root.right is None:
            return True

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
