class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # this solution uses a hash map 
        # defaultdict is used to auto assign default values to keys
        # key = letter counts, value = anagram words
        res = defaultdict(list)
        for s in strs:
            count =[0] * 26
            for c in s:     # count letters in the string
                count[ord(c) - ord('a')] += 1   # convert char to index in the array
            res[tuple(count)].append(s)     # letter count = key
        return list(res.values())   # return the groups