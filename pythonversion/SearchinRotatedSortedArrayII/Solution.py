# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
#
# Write a function to determine if a given target is in the array.

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        if not A or len(A) == 0:
            return False

        return self.searchExt(A, 0, len(A), target)

    # @param A, a list of integers
    # @param start: start index
    # @param end: end index, exclusive
    # @param target, an integer to be searched
    # @return a boolean
    def searchExt(self, A, start, end, target):
        if start > end - 1:
            return False

        while start < end:
            mid = (end + start) / 2

            if target == A[mid]:
                return True

            if A[start] < A[mid]:
                if target >= A[start] and target < A[mid]:
                    end = mid
                else:
                    start = mid + 1
            elif A[start] > A[mid]:
                if target > A[mid] and target <= A[end - 1]:
                    start = mid + 1
                else:
                    end = mid
            else:
                return self.searchExt(A, start, mid, target) or self.searchExt(A, mid + 1, end, target)
        return False
