class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        # i = index, n = value
        # enumerate allows us to use the index and value as a counter
        for i, n in enumerate(nums):
            indices[n] = i  # value of index = i

        for i, n in enumerate(nums):
            diff = target - n
            # diff in indices checks if the value diff exists in the indices
            # indices[diff] checks the index of diff
            if diff in indices and indices[diff] != i:
                # return index i and index of diff
                return [i, indices[diff]]

        return []