# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if len(a) >= len(b):
            b = b.zfill(len(a))
        else:
            a = a.zfill(len(b))

        s = zip(*[a, b])
        i = len(s) - 1
        carry = 0
        while i >= 0:
            s[i] = int(s[i][0]) + int(s[i][1]) + carry
            if s[i] == 3:
                s[i], carry = '1', 1
            elif s[i] == 2:
                s[i], carry = '0', 1
            elif s[i] == 1:
                s[i], carry = '1', 0
            else:
                s[i], carry = '0', 0
            i -= 1
        if carry == 1:
            return "1" + "".join(s)
        return "".join(s)
