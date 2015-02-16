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

        target = head.next
        head.next = None
        while target:
            temp = target.next
            target.next = None
            self.insertToSortedList(target, sentinel)
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

        pre.next = target
