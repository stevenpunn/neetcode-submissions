class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # left begins at index 0
        # right beings at last index
        left = 0
        right = len(s) - 1

        while left < right:
            # must put on a single line to complete operation at the same time
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1