# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        # solution 1
        return [ int(x) for x in str(int("".join([str(x) for x in digits])) + 1)]

        # solution 2
#         carry = 1
#         i = len(digits) - 1
#         while (i >= 0):
#             t = (digits[i] + carry) % 10
#             carry = (digits[i] + carry) / 10
#             print(carry)
#             digits[i] = t
#             i -= 1
#         digits.insert(0, carry) if carry else None
#         return digits