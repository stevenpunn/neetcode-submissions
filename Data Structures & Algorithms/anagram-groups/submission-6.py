class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict is used where a missing key starts as an empty list
        # we can append items without checking if the key exists
        res = defaultdict(list)

        # for each word, create a list of 26 zeroes, 1 slot per letter
        for s in strs:
            count = [0] * 26
            for c in s:
                # ord(c) gives each character's numeric code  
                # so subtract ord('a') to turn it into a 0-25 index
                count[ord(c) - ord('a')] += 1
            # convert list into a tuple before it's used as a key
            # dict keys need to be hashable (not changing), tuples cant change
            res[tuple(count)].append(s)
        # return the groups, the keys were only used for grouping
        return list(res.values())