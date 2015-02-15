# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array A = [1,1,1,2,2,3],
#
# Your function should return length = 5, and A is now [1,1,2,2,3].

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 2:
            return len(A)

        i = 0
        count = 1
        for j in range(1, len(A)):
            if A[i] == A[j]:
                count += 1
                continue

            if count >= 2:
                A[i+1] = A[i]
                i += 2
            else:
                i += 1
            count = 1
            A[i] = A[j]

        if count >= 2:
            A[i+1] = A[i]
            i += 1

        return i + 1
