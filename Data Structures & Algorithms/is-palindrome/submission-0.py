class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all spaces and characters and convert string to lower case and reverse\
        reversedStr = ''
        for c in s:                       # check all chars in string
            if c.isalnum():                 # if chars are numbers and/or letters
                reversedStr += c.lower()    # add lowercase character to reversed string list
        return reversedStr == reversedStr[::-1]
        if reversedStr == reversedStr:
            return True
        else:
            return False
        