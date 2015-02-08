# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        # recursive solution
        if root is None:
            return 0

        self.globalMaxPathSum = root.val

        self.getMaxSubPathSumAndUpdateGlobalMaxPathSum(root)
        return self.globalMaxPathSum

    def getMaxSubPathSumAndUpdateGlobalMaxPathSum(self, subroot):
        if subroot is None:
            return 0
        lmax = max(0, self.getMaxSubPathSumAndUpdateGlobalMaxPathSum(subroot.left))
        rmax = max(0, self.getMaxSubPathSumAndUpdateGlobalMaxPathSum(subroot.right))
        self.globalMaxPathSum = max(self.globalMaxPathSum, lmax + rmax + subroot.val)
        return max(lmax + subroot.val, rmax + subroot.val)
