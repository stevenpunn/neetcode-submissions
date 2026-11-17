class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # because we need the most recent score, we can use a stack

        # initialize an empty stack to store valid scores
        stack = []

        for op in operations:
            # sum of previous 2 scores
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            # new store that is double the previous score
            elif op == "D":
                stack.append(2 * stack[-1])
            # remove the previous score
            elif op == "C":
                stack.pop()
            # if it is a value, push it onto the stack
            else:
                stack.append(int(op))
        # return the sum of all elements in the stack
        return sum(stack)