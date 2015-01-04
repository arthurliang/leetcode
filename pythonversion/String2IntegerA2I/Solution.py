# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

plusminus = '-+'
digits = '0123456789'
whitespace = ' '
INT_MAX = 2**31 - 1
INT_MIN = -2**31

class Solution:
    # @return an integer
    def atoi(self, str):
        s = str.strip()
        l_s = len(s)

        if l_s == 0:
            return 0

        rslt = 0
        start = 1 if s[0] in plusminus else 0
        neg = True if s[0] == '-' else False

        for i in range(start, l_s):
            if s[i] not in digits:
                break
            n = digits.index(s[i])
            rslt += n
            rslt *= 10

        rslt /= 10

        if neg:
            rslt = -rslt

        if rslt > INT_MAX:
            return INT_MAX

        if rslt < INT_MIN:
            return INT_MIN

        return rslt
