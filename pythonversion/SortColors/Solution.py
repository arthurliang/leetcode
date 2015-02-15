# Given an array with n objects colored red, white or blue, sort them so that objects of
# the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue
# respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.
#
# click to show follow up.
#
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with
# total number of 0's, then 1's and followed by 2's.
#
# Could you come up with an one-pass algorithm using only constant space?

# import collections

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        # one-pass solution
        if not A:
            return

        left_index = zero_pos = 0
        right_index = len(A) - 1

        while left_index <= right_index:
            if A[left_index] == 0:
                A[left_index], A[zero_pos] = A[zero_pos], A[left_index]
                left_index += 1
                zero_pos += 1
            elif A[left_index] == 2:
                A[right_index], A[left_index] = A[left_index], A[right_index]
                right_index -= 1
            else:
                left_index += 1


#         # straight forward solution
#         if not A:
#             return
#         c = collections.Counter(A)
#         A[0 : c[0]] = [0] * c[0]
#         A[c[0] : c[0] + c[1]] = [1] * c[1]
#         A[c[0] + c[1] : c[0] + c[1] + c[2]] = [2] * c[2]
