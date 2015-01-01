# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:
    def __init__(self):
        self.backlist = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.backlist:
            self.minElement = x
        else:
            if self.minElement > x:
                self.minElement = x

        self.backlist.insert(0, x)

    # @return nothing
    def pop(self):
        self.backlist.pop(0)

    # @return an integer
    def top(self):
        return self.backlist[0]

    # @return an integer
    def getMin(self):
        return self.minElement

