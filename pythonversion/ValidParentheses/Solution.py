# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

VALIDPAIR = {')':'(', '}':'{', ']':'['}

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []

        for i in range(0, len(s)):
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if len(stack) == 0:
                    return False
                else:
                    lpair = stack.pop()
                    if lpair != VALIDPAIR.get(s[i]):
                        return False
                    else:
                        continue
            else:
                stack.append(s[i])

        return not len(stack)