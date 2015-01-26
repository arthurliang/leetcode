# Given an array and a value, remove all instances of that value in place and return the new length.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if len(A) == 0 or elem is None:
            return 0

        i = 0
        while i < len(A):
            if elem == A[i]:
                del A[i]
                continue
            i += 1

        return len(A)
