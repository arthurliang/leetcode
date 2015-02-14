# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]

import collections

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # a graph solution:
        # Set 'edge' is every char in s. Then the problem is become to find all possible paths
        # -- every path(partition) is a palindrome string -- from Node 0 to Node end.
        graph = collections.defaultdict(set)
        n = len(s)

        # construct all possible path(palindrome) from Node 0
        for i in range(n):
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    graph[i].add(j+1)

        stack, res = [[0]], []
        while stack:
            path = stack.pop()
            node = path[-1]

            if node == n:
                res.append([s[i:j] for (i, j) in zip(path[:-1], path[1:])])

            for neighbor in graph[node]:
                stack.append(path+[neighbor])

        return res


#         # another solution which is build from a list in which each single char in sting is an element
#         self.rslt = []
#         self.partitionList([c for c in s], 0)
#         return self.rslt
#
#     def partitionList(self, l, index):
#         if index == len(l) - 1:
#             self.rslt.append(l)
#             return
#
#         if l[index] == l[index + 1]:
#             p1 = l[:]
#             p1[index] = p1[index] + p1[index + 1]
#             del p1[index + 1]
#             self.partitionList(p1, index)
#
#         if index > 0 and l[index - 1] == l[index + 1]:
#             p2=l[:]
#             p2[index - 1] = p2[index - 1] + p2[index] + p2[index + 1]
#             del p2[index+1]
#             del p2[index]
#             self.partitionList(p2, index-1)
#
#         self.partitionList(l, index + 1)

#         # straight forward, DP solution
#         self.s = s
#         self.cache = {}
#         return self.partitionExt(0, len(s) - 1)
#
#     def partitionExt(self, start, end):
#         if start > end:
#             return [[]]
#
#         if start == end:
#             return [[self.s[start]]]
#
#         if (start, end) in self.cache:
#             return self.cache[(start, end)]
#
#         rslt = []
#         mid = end
#         while mid >= start:
#             if self.isPalindrome(start, mid):
#                 cur = [self.s[start:mid + 1]]
#                 rest = self.partitionExt(mid + 1, end)
#                 for r in rest:
#                     rslt.append(cur + r)
#             mid -= 1
#
#         self.cache[(start, end)] = rslt
#         return rslt
#
#     def isPalindrome(self, start, end):
#         while start < end:
#             if self.s[start] != self.s[end]:
#                 return False
#             start += 1
#             end -= 1
#         return True
