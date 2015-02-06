# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        def isValid(area):
            t = [x for x in area if x != '.']
            return len(t) == len(set(t))

        def getSubBoxByIndex(board, index):
            row = index/3 * 3
            col = index%3 * 3
            return [board[i][j] for i in range(row, row+3) for j in range(col, col+3)]

        for i in range(9):
            coli = [board[num][i] for num in range(9) ]
            sbxi = getSubBoxByIndex(board, i)
            if not isValid(board[i]) or not isValid(coli) or not isValid(sbxi):
                return False
        return True