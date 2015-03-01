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
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        sentinel = ListNode(-1)
        cur = sentinel
        carry = 0

        while l1 and l2:
            cur.next = ListNode(-1)
            cur = cur.next
            carry, cur.val= divmod((l1.val + l2.val + carry), 10)
            l1 = l1.next
            l2 = l2.next

        while carry:
            cur.next = ListNode(-1)
            cur = cur.next
            if l1:
                carry, cur.val= divmod((l1.val + carry), 10)
                l1 = l1.next
            elif l2:
                carry, cur.val= divmod((l2.val + carry), 10)
                l2 = l2.next
            else:
                cur.val = carry
                carry = 0

        return sentinel.next
