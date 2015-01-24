# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
#  [
#       [1],
#      [1,1],
#     [1,2,1],
#    [1,3,3,1],
#   [1,4,6,4,1]
#  ]

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        rslt = self.generate(numRows - 1)
        rslt.append(self.generateRowByUpperRow(rslt[-1]))
        return rslt

    def generateRowByUpperRow(self, upperRow):
        rslt = [1]
        for i in range(0, len(upperRow) - 1):
            rslt.append(upperRow[i] + upperRow[i + 1])
        rslt.append(1)
        return rslt
