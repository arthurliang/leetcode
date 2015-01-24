# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head is None or n == 0:
            return head
        l = []
        p = head
        while p is not None:
            l.append(p)
            p = p.next
        if len(l) == 1 and n == 1:
            return None
        if n == 1:
            l[-(n+1)].next = None
        elif n == len(l):
            head = head.next
        else:
            l[-(n+1)].next = l[-(n-1)]
        return head