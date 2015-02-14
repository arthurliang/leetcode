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

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # straight forward, DP
        self.s = s
        self.cache = {}
        return self.partitionExt(0, len(s) - 1)

    def partitionExt(self, start, end):
        if start > end:
            return [[]]

        if start == end:
            return [[self.s[start]]]

        if (start, end) in self.cache:
            return self.cache[(start, end)]

        rslt = []
        mid = end
        while mid >= start:
            if self.isPalindrome(start, mid):
                cur = [self.s[start:mid + 1]]
                rest = self.partitionExt(mid + 1, end)
                for i in range(len(rest)):
                    rslt.append(cur + rest[i])
            mid -= 1

        self.cache[(start,end)] = rslt
        return rslt

    def isPalindrome(self, start, end):
        while start < end:
            if self.s[start] != self.s[end]:
                return False
            start += 1
            end -= 1
        return True
