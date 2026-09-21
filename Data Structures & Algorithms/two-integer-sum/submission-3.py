class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):    # i = index, n = value
            indices[n] = i      # stores the number as the key and index as value

        for i, n in enumerate(nums):    # iterate to find pair
            diff = target - n       # number needed to reach charger
            # check if the needed values exist
            # indices[diff] != i makes sure we don't use the same element twice
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []