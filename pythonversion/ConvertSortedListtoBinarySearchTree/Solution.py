# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utility.BinTree import TreeNode

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        self.curSLLhead = head
        return self.genBST(self.getSizeOfSLList(head))

    def getSizeOfSLList(self, head):
        if head is None:
            return 0
        l = 1
        while head.next:
            head = head.next
            l += 1
        return l

    def genBST(self, length):
        if length == 0:
            return None

        if length == 1:
            root = TreeNode(self.curSLLhead.val)
            self.curSLLhead = self.curSLLhead.next
            return root

        root = TreeNode(0)
        root.left = self.genBST(length / 2)
        root.val = self.curSLLhead.val
        self.curSLLhead = self.curSLLhead.next
        root.right = self.genBST(length - length / 2 - 1)

        return root
