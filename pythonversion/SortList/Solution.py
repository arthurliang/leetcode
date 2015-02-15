# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utility.CustomList import ListNode

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        newhead = ListNode(-1)
        tmphead = ListNode(-1)

        newhead.next = head

        step = 1
        finished = False
        while not finished:
            head = newhead.next
            firstIter = True
            pre = None
            prelast = None
            while head:
                ha = head
                for i in range(step):
                    if head:
                        pre = head
                        head = head.next
                    else:
                        break

                if head is None:
                    if firstIter:
                        finished = True
                    break

                pre.next = None

                hb = head
                for i in range(step):
                    if head:
                        pre = head
                        head = head.next
                    else:
                        break
                pre.next = None

                last = self.bottomUpMerge(ha, hb, tmphead)
                last.next = head

                if prelast:
                    prelast.next = tmphead.next
                prelast = last

                if firstIter:
                    newhead.next = tmphead.next
                    firstIter = False

            step *= 2

        return newhead.next

    def bottomUpMerge(self, ha, hb, newHead):
        t = newHead

        while ha and hb:
            if ha.val < hb.val:
                t.next = ha
                ha = ha.next
            else:
                t.next = hb
                hb = hb.next
            t = t.next

        if ha is not None:
            t.next = ha
        if hb is not None:
            t.next = hb

        while t and t.next:
            t = t.next
        return t

