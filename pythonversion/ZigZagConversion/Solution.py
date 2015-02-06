# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like
# this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if (nRows == 1) or (len(s) <= nRows):
            return s

        shuttle = 0
        reversionSwitch = False
        strTable = []

        for i in range(0, nRows):
            strTable.append("")

        for i in range(0, len(s)):
            strTable[shuttle] += (s[i])

            shuttle = shuttle - 1 if reversionSwitch else shuttle + 1

            if (shuttle == 0) or shuttle == (nRows - 1):
                reversionSwitch = not reversionSwitch

        return "".join(strTable)
