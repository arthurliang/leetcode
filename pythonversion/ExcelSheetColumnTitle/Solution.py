# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#    27 -> AA
#     28 -> AB
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.

class Solution:
    # @return a string
    def convertToTitle(self, num):
        Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = ''
        n = num
        while n > 0:
            m = n % 26
            if m == 0:
                m = 26
            s = Uppercase[m-1] + s
            n = int((n - m) / (26))
        return s