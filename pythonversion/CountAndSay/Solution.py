# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.

class Solution:
    # @return a string
    def countAndSay(self, n):
        base = ""
        while n != 0:
            base = self.caountAndSayStr(base)
            n -= 1

        return base


    def caountAndSayStr(self, s):
        if s == "":
            return "1"
        if s == "1":
            return "11"

        rslt = ""
        num = 1
        cur = s[0]

        index = 1
        sl = len(s)

        while index != sl:
            if s[index] == cur:
                num += 1
            else:
                rslt += str(num) + cur
                num = 1
                cur = s[index]
            index += 1

        rslt += str(num) + cur

        return rslt
