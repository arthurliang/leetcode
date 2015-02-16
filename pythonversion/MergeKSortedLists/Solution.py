# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utility.CustomList import ListNode
import heapq

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        # heapq from std lib solution
        if lists is None:
            return None

        c = sentinel = ListNode(-1)

        minHeap = [(node.val, node) for node in lists if node]
        heapq.heapify(minHeap)

        while minHeap:
            node = heapq.heappop(minHeap)[1]
            c.next = node
            c = c.next
            if c.next:
                heapq.heappush(minHeap, (c.next.val, c.next))

        return sentinel.next


#         # Merge Sort likely solution
#         if lists is None or len(lists) == 0:
#             return None
#
#         sentinel = ListNode(-1)
#
#         while len(lists) != 1:
#             lists.insert(0, self.bottomUpMerge(lists.pop(), lists.pop(), sentinel))
#
#         return lists[0]
#
#
#     def bottomUpMerge(self, A, B, sentinel):
#         c = sentinel
#         while A and B:
#             if A.val <= B.val:
#                 c.next = A
#                 A = A.next
#             else:
#                 c.next = B
#                 B = B.next
#             c = c.next
#
#         if A is None:
#             c.next = B
#         if B is None:
#             c.next = A
#
#         return sentinel.next
