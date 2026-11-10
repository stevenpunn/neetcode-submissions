class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # start with the first string as the candidate
        # compare with each subsequent string, shrinking prefix to match common pref

        # prefix is initalized as the first string in the array
        prefix = strs[0]

        # compare each string to the current prefix array we have
        for i in range(1, len(strs)):
            j = 0   # j represents where characters stop matching
            while j < min(len(prefix), len(strs[i])):
                # find where index j stops matching characters
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            # truncate prefix to include only characters from index 0 to j-1
            prefix = prefix[:j]
        return prefix