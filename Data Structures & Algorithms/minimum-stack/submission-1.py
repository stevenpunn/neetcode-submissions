class MinStack:

    def __init__(self):
        self.stack = []     # initialize our stack
        self.minStack = []  # this is our minStack

    def push(self, val: int) -> None:
        # push the val onto the stack
        self.stack.append(val)
        # compute the new min between val and current min on minStack
        val = min(val, self.minStack[-1] if self.minStack else val)
        # append this value to minStack
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()    # pop from both stack and minStack
        self.minStack.pop()

    def top(self) -> int:
        # return the top of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # return top of minStack, which is the current min
        return self.minStack[-1]