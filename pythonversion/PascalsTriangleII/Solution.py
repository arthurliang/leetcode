# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        l = [[1], [1, 1]]
        if rowIndex == 0 or rowIndex == 1:
            return l[rowIndex]

        upperRow = self.getRow(rowIndex - 1)

        rslt = [1]
        for i in range(0, len(upperRow) - 1):
            rslt.append(upperRow[i] + upperRow[i + 1])
        rslt.append(1)
        return rslt
