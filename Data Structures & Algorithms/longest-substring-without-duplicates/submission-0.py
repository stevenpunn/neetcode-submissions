class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # want O(n) time, O(m) space
        # use a sliding window, keep 1 window that tracks unique characters
        # left pointer, move right pointer
        # if there is a repeated character move the left pointer until repeated character is gone
        charSet = set()         # empty charSet
        l = 0                   # left pointer 
        res = 0 

        for r in range(len(s)):             # right pointer to move through the string
            while s[r] in charSet:          # while s[r] is already in the charSet, is found before
                charSet.remove(s[l])        # remove the left pointer
                l += 1                      # move l to the right
            charSet.add(s[r])               # add the right pointer to the set
            res = max(res, r - l + 1)       # result = window size, or 0 if invalid
        return res 