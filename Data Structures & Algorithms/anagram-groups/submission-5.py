class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # find groups of words by sorted strings
        # we can use a hashtable to store character counts

        # using defaultdict, accessing a key that doesn't yet exist 
        # creates ley w/ default value
        result = defaultdict(list)
        for s in strs:
            # sorted(s) returns a sorted list of characters 
            # ''.join() then joins them together into a string
            # we need to join because lists can't be dictionary keys
            sortedS = ''.join(sorted(s))
            # this appends the strings together into the dictionary
            result[sortedS].append(s)
        # .values() 
        return list(result.values())