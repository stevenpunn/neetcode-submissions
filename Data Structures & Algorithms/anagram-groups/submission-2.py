from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # aim for O(m * n)
        # use a hashmap, check if each combination of letters is in the hashmap
        anagram_map = defaultdict(list)
        res = []

        # go through each word, check if its an anagram
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)

        for value in anagram_map.values():
            res.append(value)
        
        return res