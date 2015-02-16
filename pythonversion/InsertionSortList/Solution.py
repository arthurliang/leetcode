# Sort a linked list using insertion sort.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utility.CustomList import ListNode

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head

        sentinel = ListNode(-1)
        sentinel.next = head

        pre = head
        target = head.next
        while target:
            while pre and target and pre.val < target.val:
                pre = target
                target = target.next
            if target is None:
                break

            temp = target.next
            pre.next = None
            target.next = None

            if target.val < sentinel.next.val:
                target.next = sentinel.next
                sentinel.next = target
            else:
                self.insertToSortedList(target, sentinel)

            pre.next = temp
            target = temp

        return sentinel.next

    def insertToSortedList(self, target, sentinel):
        pre = sentinel
        head = sentinel.next
        while head:
            if target.val <= head.val:
                target.next = head
                pre.next = target
                return
            pre = head
            head = head.next
