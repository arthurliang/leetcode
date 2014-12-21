class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        tempStr = s.rstrip()

        if tempStr == '':
            return 0

        word_list = tempStr.split(' ')

        return len(word_list[-1])
