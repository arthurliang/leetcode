# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#    A -> 1
#    B -> 2
#    C -> 3
#    ...
#    Z -> 26
#    AA -> 27
#    AB -> 28
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        Uppercase = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = 0

        for i in range(0, len(s)):
            num += Uppercase.index(s[i])
            i += 1
            num *= 26

        return num / 26
