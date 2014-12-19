class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows is 1 or len(s) <= nRows:
            return s

        shuttle = 0
        reversionSwitch = False
        strTable = []

        for i in range(0, nRows):
            strTable.append("")

        for i in range(0, len(s)):
            strTable[shuttle] += (s[i])

            shuttle = shuttle - 1 if reversionSwitch else shuttle + 1

            if shuttle is 0 or shuttle is nRows - 1:
                reversionSwitch = not reversionSwitch

        return "".join(strTable)
