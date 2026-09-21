class Solution:
    def isValid(self, s: str) -> bool:
        # O(n)
        # use a stack with a LIFO approach
        # the stack will track opening brackets, 
        stack = []      # stack stores opening brackets
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False