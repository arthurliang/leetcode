# Given a sorted array, remove the duplicates in place such that each element appear only once and
# return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array A = [1,1,2],
#
# Your function should return length = 2, and A is now [1,2].
#
# Note:
# del, pop(), or remove() are not allowed.

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        len_A = len(A)
        cur_index = 0
        offset = 0
        j = 0
        while cur_index + offset < len_A:
            j = cur_index + offset + 1
            while j < len_A and A[cur_index] == A[j]:
                j += 1
                offset = j - cur_index - 1
            if j < len_A:
                A[cur_index + 1] = A[j]
            cur_index += 1

        return cur_index
