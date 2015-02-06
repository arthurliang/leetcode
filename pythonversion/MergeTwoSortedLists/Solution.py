# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from utility.CustomList import ListNode

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        # solution 2
        rslt = ListNode(-1)
        cp = rslt
        while (l1 and l2):
            if l1.val <= l2.val:
                cp.next = l1
                l1 = l1.next
            else:
                cp.next = l2
                l2 = l2.next
            cp = cp.next
        l3 = l1 if l1 is not None else l2
        cp.next = l3
        return rslt.next

        # solution 1
#         if l1 == None:
#             return l2
#         if l2 == None:
#             return l1
#         rslt, waitInsertNode = (l1, l2) if l1.val <= l2.val else (l2, l1)
#         curPointer = rslt
#
#         while waitInsertNode and curPointer.next:
#             if curPointer.next.val <= waitInsertNode.val:
#                 curPointer = curPointer.next
#             else:
#                 t = curPointer.next
#                 curPointer.next = waitInsertNode
#                 waitInsertNode = t
#                 curPointer = curPointer.next
#
#         if curPointer.next is None:
#             curPointer.next = waitInsertNode
#         return rslt