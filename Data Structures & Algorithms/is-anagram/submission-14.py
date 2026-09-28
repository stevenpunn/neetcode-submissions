class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can use a hashmap to determine if they have the same character counts

        # first check the basecase, both strings have to have the same length
        if len(s) != len(t):
            return False

        # creates 2 hashmaps for each string
        countS = {}
        countT = {}

        # iterate through both strings at the same time
        for i in range(len(s)):
            # increase the character counts for both s[i] and t[i] in both maps
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

