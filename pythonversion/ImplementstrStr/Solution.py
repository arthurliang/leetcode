# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Update (2014-11-02):
# The signature of the function had been updated to return the index instead of the pointer. If you still
# see your function signature returns a char * or String, please click the reload button  to reset your
# code definition.

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0

        rslt = 0
        valid = False

        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                for j in range(0, len(needle)):
                    if haystack[i + j] == needle[j]:
                        continue
                    else:
                        j = len(needle)
                        break
                if j == len(needle) - 1:
                    valid = True
                    rslt = i
                    break

        if valid:
            return rslt
        return -1
