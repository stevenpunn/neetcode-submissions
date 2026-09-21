class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n + m)
        # base case, if not same, then cannot be anagrams
        if len(s) != len(t):
            return False
        
        # maintain hashmaps for both strings
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # count each occurrance in S
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT