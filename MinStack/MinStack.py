# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:
    def __init__(self):
        self.backendlist = []
        self.__min = None

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.backendlist:
            self.__min = x
        else:
            if self.__min > x:
                t = self.__min - x
                self.__min = x
                x = x - t

        self.backendlist.append(x)

    # @return nothing
    def pop(self):
        if not self.backendlist:
            return None

        x = self.backendlist.pop()
        if x < self.__min:
            self.__min = self.__min + self.__min - x

    # @return an integer
    def top(self):
        if not self.backendlist:
            return None

        x = self.backendlist.pop()
        self.backendlist.append(x)
        return max(self.__min, x)

    # @return an integer
    def getMin(self):
        return self.__min

