class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # create a dictionary to check if c has a closing bracket, and gives opening bracket to match
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        # iterate through the string 
        for c in s:
            if c in closeToOpen:    # if this is a closing bracket, 
                # check if stack not empty and top of stack matches opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()         # if it matches, remove it
                else:
                    return False    # wrong type or nothing matches
            else:
                stack.append(c)     # detected opening bracket, wait for a match
            
        return True if not stack else False # returns true only if all opening brackets are closed