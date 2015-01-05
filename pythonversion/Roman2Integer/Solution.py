# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return an integer
    def romanToInt(self, s):
        rslt = 0
        i = 0
        while i < len(s):
            if s[i] == 'I':
                if i != len(s) - 1 and s[i+1] in 'VX':
                    rslt += 4 if s[i+1] == 'V' else 9
                    i += 2
                    continue
                rslt += 1
            if s[i] == 'X':
                if i != len(s) - 1 and s[i+1] in 'LC':
                    rslt += 40 if s[i+1] == 'L' else 90
                    i += 2
                    continue
                rslt += 10
            if s[i] == 'C':
                if i != len(s) - 1 and s[i+1] in 'DM':
                    rslt += 400 if s[i+1] == 'D' else 900
                    i += 2
                    continue
                rslt += 100
            if s[i] == 'M':
                rslt += 1000
            if s[i] == 'V':
                rslt += 5
            if s[i] == 'L':
                rslt += 50
            if s[i] == 'D':
                rslt += 500
            i += 1

        return rslt
