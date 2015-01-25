# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        rslt = 0

        while n > 0:
            n = int(n / 5)
            rslt += n

        return rslt

# According to the result, we can figure out the algorithm:
# Numbers of zeros can be plus 1 'i' times when n has 'i' numbers of factor 5
#
# ------------start-------------
# n is 5, Zeroes is 1
# n is 10, Zeroes is 2
# n is 15, Zeroes is 3
# n is 20, Zeroes is 4
# n is 25, Zeroes is 6
# n is 30, Zeroes is 7
# n is 35, Zeroes is 8
# n is 40, Zeroes is 9
# n is 45, Zeroes is 10
# n is 50, Zeroes is 12
# n is 55, Zeroes is 13
# n is 60, Zeroes is 14
# n is 65, Zeroes is 15
# n is 70, Zeroes is 16
# n is 75, Zeroes is 18
# n is 80, Zeroes is 19
# n is 85, Zeroes is 20
# n is 90, Zeroes is 21
# n is 95, Zeroes is 22
# n is 100, Zeroes is 24
# n is 105, Zeroes is 25
# n is 110, Zeroes is 26
# n is 115, Zeroes is 27
# n is 120, Zeroes is 28
# n is 125, Zeroes is 31
# n is 130, Zeroes is 32
# n is 135, Zeroes is 33
# n is 140, Zeroes is 34
# n is 145, Zeroes is 35
# n is 150, Zeroes is 37
# n is 155, Zeroes is 38
# n is 160, Zeroes is 39
# n is 165, Zeroes is 40
# n is 170, Zeroes is 41
# n is 175, Zeroes is 43
# n is 180, Zeroes is 44
# n is 185, Zeroes is 45
# n is 190, Zeroes is 46
# n is 195, Zeroes is 47
# n is 200, Zeroes is 49
# -------------end--------------
