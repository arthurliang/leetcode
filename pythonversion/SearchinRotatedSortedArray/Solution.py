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

        if A[start] < A[end - 1]:
            return self.binsearch(A, start, end, target)

        mid = (end + start) / 2

        if target < A[start]:
            if A[mid] < target:
                return self.binsearch(A, mid + 1, end, target)
            elif A[mid] > target:
                if A[mid] > A[start]:
                    return self.searchExt(A, mid + 1, end, target)
                else:
                    return self.searchExt(A, start + 1, mid, target)
            else:
                return mid

        elif target > A[start]:
            if A[mid] > target:
                return self.binsearch(A, start + 1, mid, target)

            elif A[mid] < target:
                if A[mid] > A[start]:
                    return self.searchExt(A, mid + 1, end, target)
                else:
                    return self.searchExt(A, start + 1, mid, target)
            else:
                return mid
        else:
            return start


    # @param A, a list of integers
    # @param start: start index
    # @param end: end index, exclusive
    # @param target, an integer to be searched
    # @return an integer
    def binsearch(self, A, start, end, target):
        if end - 1 < start:
            return -1

        mid = (end + start) / 2
        if A[mid] > target:
            return self.binsearch(A, start, mid, target)
        elif A[mid] < target:
            return self.binsearch(A, mid + 1, end, target)
        else:
            return mid
