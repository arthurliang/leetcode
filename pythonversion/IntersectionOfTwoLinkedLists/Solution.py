# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 ¡ú a2
#                    ¨K
#                      c1 ¡ú c2 ¡ú c3
#                    ¨J
# B:     b1 ¡ú b2 ¡ú b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# Credits:
# Special thanks to @stellari for adding this problem and creating all test cases.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        pA = headA
        pB = headB

        while pA and pB:
            pA = pA.next
            pB = pB.next

        while pA:
            headA = headA.next
            pA = pA.next

        while pB:
            headB = headB.next
            pB = pB.next

        while headA is not None and headA != headB:
            headA = headA.next
            headB = headB.next

        return headA