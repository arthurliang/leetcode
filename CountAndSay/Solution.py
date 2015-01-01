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
