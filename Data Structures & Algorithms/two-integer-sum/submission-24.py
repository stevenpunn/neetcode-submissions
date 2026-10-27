class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        # first iterate through nums using index i and each element n
        for i, n in enumerate(nums):
            # compute the difference for the current element
            diff = target - n
            # if the complement exists in the map, return the complement and current index
            if diff in prevMap:
                return [prevMap[diff], i]
            # if this does not return, assign the value to the index
            prevMap[n] = i