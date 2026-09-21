class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # ans returns result array of size 2n
        ans = [0] * (2 * n)
        # iterate through input array using index i from 0 to n-1
        for i, num in enumerate(nums):
            # set ans[i] = nums[i]
            # set ans[i + n] to nums[i]
            ans[i] = ans[i + n] = num
        return ans