class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # represent each string as a frequency of its characters
        # create a hashmap, each key is a 26-length tuple
        res = defaultdict(list)
        for s in strs:
            # for each string in the input
            # initialize a count array of size 26 of all 0s
            count = [0] * 26
            # for each character in the string
            for c in s:
                # increment count at the corresponding index
                count[ord(c) - ord('a')] += 1
            # convert count array to a tuple, use it as the key
            res[tuple(count)].append(s)
        return list(res.values())