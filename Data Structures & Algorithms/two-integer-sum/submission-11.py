class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                # by returning like this, it returns the index of the previously found value first, and the current index last
                return [prevMap[diff], i]
            # after each iteration, it stores each value in the prevMap with the corresponding index
            prevMap[n] = i  