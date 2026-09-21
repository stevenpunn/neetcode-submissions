class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case, if both strings are not the same length, return false
        if len(s) != len(t):
            return False
        
        # rather than sorting, use hash maps to count character frequencies
        countS, countT = {}, {}

        # iterate through both strings and increase char count for s[i] and t[i]
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        #return countS == countT
        if countS == countT:
            return True
        else:
            return False
        # Time: O(n + m), n = len string s, m = len of string t
        # Space: O(1)