class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can use a hashmap to found character frequencies and see if they match

        # first have the base case, if the length does not match, return false
        if len(s) != len(t):
            return False
        
        # each count gets a hash map to count the character and its frequency
        countS = {}
        countT = {}

        # iterate through the entire length of the first string
        for i in range(len(s)):
            # increase the character count through both s[i] and t[i] in the first and second map
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # if their counts match, then return true
        if countS == countT:
            return True
        else:
            return False