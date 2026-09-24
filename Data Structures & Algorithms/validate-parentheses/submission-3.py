class Solution:
    def isValid(self, s: str) -> bool:
        # stack will store opening brackets
        stack = []
        closeToOpen = {")": "(", "]" : "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                # if it is a closing bracket, check if the stack is not empty
                # and that its top matches the corresponding opening cracket
                if stack and stack[-1] == closeToOpen[c]:
                    # pop the stack if it does
                    stack.pop()
                else:
                    # return false if not
                    return False
            else:
                # if it is an opening bracket, push onto stack
                stack.append(c)
        
        return True if not stack else False