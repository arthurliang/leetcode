# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utility.CustomList import ListNode

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None or l2 is None:
            return None

        rslt = ListNode(-1)
        rslt.val = l1.val + l2.val
        return rslt
