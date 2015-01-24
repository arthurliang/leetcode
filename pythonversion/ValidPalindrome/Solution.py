# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
#  "A man, a plan, a canal: Panama" is a palindrome.
#  "race a car" is not a palindrome.
#
# Note:
#  Have you consider that the string might be empty? This is a good question to ask during an interview.
#
#  For the purpose of this problem, we define empty string as valid palindrome.

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        UppercaseNumber = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s = s.upper()
        wait4processStr = ""

        for i in range(0, len(s)):
            if s[i] in UppercaseNumber:
                wait4processStr += s[i]

        for j in range(0, len(wait4processStr)/2):
            if wait4processStr[j] != wait4processStr[-(j+1)]:
                return False

        return True