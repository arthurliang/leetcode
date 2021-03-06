# Given a linked list and a value x, partition it such that all nodes
# less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each
# of the two partitions.
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utility.CustomList import ListNode

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        # 2nd solution
        rslt = ListNode(0)
        temp = ListNode(1)

        lesslist = rslt
        greatlist = temp

        while head:
            if head.val < x:
                lesslist.next = head
                lesslist = lesslist.next
            else:
                greatlist.next = head
                greatlist = greatlist.next

            head = head.next

        greatlist.next = None
        lesslist.next = temp.next
        return rslt.next

#         # 1st solution
#         rslt = ListNode(0)
#         rslt.next = head
#
#         less = rslt
#         greater = None
#
#         while head:
#             if head.val >= x:
#                 greater = head
#                 head = head.next
#             elif greater is None:
#                 less = head
#                 head = head.next
#             else:
#                 greater.next = head.next
#                 head.next = less.next
#                 less.next = head
#                 less = head
#                 head = greater.next
#
#         return rslt.next
