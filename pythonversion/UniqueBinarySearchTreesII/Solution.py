# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
#
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from utility.BinTree import TreeNode

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        self.cache = {}
        return self.generate(1, n)

    def generate(self, min, max):
        if (min, max) in self.cache:
            return self.cache[(min, max)]

        elif max < min:
            self.cache[(min, max)] = [None]

        elif max == min:
            self.cache[(min, max)] = [TreeNode(max)]

        else:
            nodes = []
            for i in range(min, max + 1):
                for left in self.generate(min, i - 1):
                    for right in self.generate(i + 1, max):
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        nodes.append(root)

            self.cache[(min, max)] = nodes

        return self.cache[(min, max)]
