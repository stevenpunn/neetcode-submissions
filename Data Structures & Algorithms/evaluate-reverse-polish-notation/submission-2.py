class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we can do this using a stack
        # when we see a number, push it onto the stack
        # when we see an operator, pop the top 2 numbers, apply the operation and push the result

        # first create an empty stack
        stack = []

        # for each token, if it is a number, pop the top 2 numbers
        # then apply the operator in the correct order
        # push the result back onto the stack
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                # if c is a number, convert to an integer and push it onto the stack
                stack.append(int(c))
        return stack[0]
