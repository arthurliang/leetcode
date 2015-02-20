# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Credits:
# Special thanks to @Shangrila for adding this problem and creating all test cases.

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return "error"

        rslt = '' if numerator * denominator >= 0 else '-'

        numerator = abs(numerator)
        denominator = abs(denominator)

        rslt += str(numerator / denominator)

        r = numerator % denominator
        if r == 0:
            return rslt

        rslt += '.'
        remainderCache = {}

        while r not in remainderCache and r != 0:
            remainderCache[r] = len(rslt)

            r *= 10
            quotient = r / denominator
            r = r % denominator

            if r in remainderCache:
                rslt = rslt[:remainderCache[r]] + '(' + rslt[remainderCache[r]:] + str(quotient) + ')'
                return rslt

            rslt += str(quotient)


        return  rslt


#         print("{:-^30}".format("center"))
#         n, remainder = divmod(abs(numerator), abs(denominator))
#         sign = '-' if numerator*denominator < 0 else ''
#         result = [sign+str(n), '.']
#         stack = []
#         print stack
#         while remainder not in stack:
#             stack.append(remainder)
#             print stack
#             n, remainder = divmod(remainder*10, abs(denominator))
#             print n, remainder
#             result.append(str(n))
#
#         print result
#         idx = stack.index(remainder)
#         result.insert(idx+2, '(')
#         result.append(')')
#         print result
#         return ''.join(result).replace('(0)', '').rstrip('.')
