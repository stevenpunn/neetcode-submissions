class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # use a stack, the most recent numbers are always used first
        # if we see a num, push it onto the stack
        # when we see an operator, pop the top 2 nums, apply the operation, push the result back
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            # must find a, b first since subtraction is in a specific order
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
            # number, not operator, so convert to int and push onto stack
                stack.append(int(c))
        # when processed all tokens, stack contains only 1 value, so return it
        return stack[0]