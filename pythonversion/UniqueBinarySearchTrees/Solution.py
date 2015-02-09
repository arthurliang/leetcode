# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution:
    # @return an integer
    def numTrees(self, n):
        # iterative solution:
        if n == 0:
            return 0

        F = [0] * (n + 1)
        F[0:2] = [1, 1]
        i = 2
        while i <= n:
            for j in range(i):
                F[i] += F[j] * F[i - 1 - j]
            i += 1
        return F[n]


#         # recursive solution
#         if n == 0:
#             return 0
#
#         return self.numTreesWhichNumLTzero(n)
#
#     def numTreesWhichNumLTzero(self, n):
#         # Fn = F0*Fn-1 + F1*Fn-2 + ... + Fn-2*F1 + Fn-1*F0
#         # F0 =1, F1 = 1
#         if n <= 1:
#             return 1;
#
#         rslt = 0
#         i = 0
#         while i < n:
#             rslt = rslt + self.numTreesWhichNumLTzero(i) * self.numTreesWhichNumLTzero(n - 1 - i)
#             i += 1
#
#         return rslt

