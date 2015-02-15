# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if not A or len(A) == 0:
            return -1

        return self.searchExt(A, 0, len(A), target)

    # @param A, a list of integers
    # @param start: start index
    # @param end: end index, exclusive
    # @param target, an integer to be searched
    # @return an integer
    def searchExt(self, A, start, end, target):
        if start > end - 1:
            return -1

        while start < end:
            mid = (end + start) / 2

            if target == A[mid]:
                return mid

            if A[start] < A[mid]:
                if target >= A[start] and target < A[mid]:
                    end = mid
                else:
                    start = mid + 1
            else:
                if target > A[mid] and target <= A[end - 1]:
                    start = mid + 1
                else:
                    end = mid

        return -1


