# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n = len(s)
        palindrome = [[False for i in range(n)] for j in range(n)]
        minCutCache = [n - 1 for i in range(n)]

        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or palindrome[j + 1][i - 1]):
                    palindrome[j][i] = True
                    minCutCache[i] = min(minCutCache[i], minCutCache[j - 1] + 1) if j != 0 else 0

        return minCutCache[n - 1]
