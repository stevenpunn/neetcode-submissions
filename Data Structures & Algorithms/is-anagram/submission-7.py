class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can use a hashmap to found character frequencies and see if they match

        # first have the base case, if the length does not match, return false
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        if countS == countT:
            return True
        else:
            return False