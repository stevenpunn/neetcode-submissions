class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # i, j = start of each string, res = result list
        i, j = 0, 0
        result = []

        while i < len(word1) and j < len(word2):
            # append current index of each word alternatively
            # then go to the next index
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        # if len(word1) != len(word2), 
        # append remaining characters to the end of the result
        result.append(word1[i:])
        result.append(word2[j:])
        # return the joined result string
        return "".join(result)