class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram = same characters, not in reverse
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        # sorted returns each character alphabetically sorted
        # this is fine for anagrams since order doesn't matter
        