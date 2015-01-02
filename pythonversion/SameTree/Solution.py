# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False

        valCompare = (p.val == q.val)
        leftTreeCompare = self.isSameTree(p.left, q.left)
        rightTreeCompare = self.isSameTree(p.right, q.right)

        return valCompare and leftTreeCompare and rightTreeCompare