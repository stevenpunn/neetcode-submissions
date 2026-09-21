class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ex: ate has 1a, 1t, 1e, store that and compare
        # can use a Hashmap to store values. Keys will be anagrams, values will be strings
        result = defaultdict(list) # map charCount to list of anagrams

        for s in strs:                  # loops through all strings given
            count = [0] * 26            # count storing each character

            for c in s:                             # counts how many characters in each string
                count[ord(c) - ord('a')] += 1       # map a to 0, z to 26

            result[tuple(count)].append(s)
                
        return result.values()

        # O(m*n)            m = # of strings        n = avg length of each string
