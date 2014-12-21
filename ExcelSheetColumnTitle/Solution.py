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