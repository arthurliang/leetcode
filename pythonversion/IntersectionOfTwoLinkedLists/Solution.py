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