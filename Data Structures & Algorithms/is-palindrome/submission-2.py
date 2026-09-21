class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        if newStr[::-1] == newStr:
            return True
        else:
            return False
            