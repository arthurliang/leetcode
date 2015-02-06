# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return
# the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        tempStr = s.rstrip()

        if tempStr == '':
            return 0

        word_list = tempStr.split(' ')

        return len(word_list[-1])
