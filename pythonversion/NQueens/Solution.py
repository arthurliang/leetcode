# -*- coding: utf-8 -*-
# The n-queens puzzle is the problem of placing n queens on an n��n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

# Memo for Queen's puzzle
class Memo:
    def __init__(self, n, row):
        self.n = n
        self.pos = 0
        self.row = row
        self.ancestor = None

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.result = []
        self.backtrace(Memo(n, 0))
        return self.result

    def backtrace(self, memo):
        for pos in range(memo.n):

            memo.pos = pos
            if self.reject(memo):
                continue

            memo.row += 1

            if self.accept(memo):
                self.outPut(memo)
            else:
                newMemo = Memo(memo.n, memo.row)
                memo.row -= 1
                newMemo.ancestor = memo
                self.backtrace(newMemo)

    def reject(self, memo):
        if memo.ancestor is None:
            return False

        ancestor = memo.ancestor
        posLeft = memo.pos
        posRight = memo.pos
        while ancestor:
            if ancestor.pos == memo.pos:
                break

            posLeft -= 1
            if ancestor.pos == posLeft:
                break

            posRight += 1
            if ancestor.pos == posRight:
                break

            ancestor = ancestor.ancestor

        if ancestor:
            return True
        return False

    def accept(self, memo):
        return memo.row == memo.n

    def outPut(self, memo):
        solution = []
        while memo:
            solution.insert(0,"".join(['.' if i != memo.pos else 'Q' for i in range(memo.n)]))
            memo = memo.ancestor
        self.result.append(solution)
