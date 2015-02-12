# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise
# a constant space solution?

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utility.BinTree import TreeNode

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        if root is None:
            return root

        self.fstWrong = self.secWrong = TreeNode(None)

#         # Below code can replace upper line when in OJ
#         self.fstWrong = root
#         while self.fstWrong.left:
#             self.fstWrong = self.fstWrong.left
#         self.secWrong = self.fstWrong

        self.fstWrongLocked = self.secWrongLocked = False

        self.findWrongByInorderTraversal(root)

        if self.fstWrongLocked:
            t = self.fstWrong.val
            self.fstWrong.val = self.secWrong.val
            self.secWrong.val = t

        return root

    def findWrongByInorderTraversal(self, root):
        if self.fstWrongLocked and self.secWrongLocked:
            return

        if root.left is not None:
            self.findWrongByInorderTraversal(root.left)

        if not self.fstWrongLocked:
            if self.fstWrong.val <= root.val:
                self.fstWrong = root
            else:
                self.secWrong = root
                self.fstWrongLocked = True

        if not self.secWrongLocked:
            if self.secWrong.val < self.fstWrong.val and self.fstWrong.val < root.val:
                self.secWrongLocked = True
            else:
                self.secWrong = root

        if root.right is not None:
            self.findWrongByInorderTraversal(root.right)
