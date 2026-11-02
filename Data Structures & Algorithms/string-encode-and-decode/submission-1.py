class Solution:

    def encode(self, strs: List[str]) -> str:
        # initialize an empty array to store the result
        res = []
        for s in strs:
            # compute the length of each string, append 'length#string' to the builder
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        # return the final encoded string
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # an empty list for the decoded strings
        res = []
        i = 0

        # while i is in the bounds of the encoded string
        while i < len(s):
            j = i
            # move pointer j until it finds #: this is the length
            while s[j] != '#':
                j += 1
            # convert the substring into an integer 'length'
            length = int(s[i:j])
            # move i to the character right after #
            i = j + 1
            # extract the length characters
            j = i + length
            # append the string to the result list
            res.append(s[i:j])
            # move i forward by length to decode the next segment 
            i = j

        return res