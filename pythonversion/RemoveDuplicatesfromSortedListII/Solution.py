# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utility.CustomList import ListNode

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        sentinel = pre = ListNode(-1)
        sentinel.next = head
        p1, p2 = head, head
        count = 0

        while p2 is not None:
            if p1.val == p2.val:
                count += 1
                p2 = p2.next
                continue
            if count > 1:
                pre.next = p2
                p1 = p2
            else:
                pre = p1
                p1 = p2
            count = 0

        if count > 1:
            pre.next = p2
        return sentinel.next
