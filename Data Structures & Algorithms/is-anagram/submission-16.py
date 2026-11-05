class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case: determine if the string lengths are the same
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            # increase the character count for s[i] and t[i] in the first and second map
            # s[i] is the current character 
            # countS.get(s[i], 0) looks up how many times we've seen the current character
            # .get(key, default) returns stored value if it exists
            # then we add 1 for each occurrence
            # countS[s[i]] stores the count
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        if countS == countT:
            return True
        else:
            return False
