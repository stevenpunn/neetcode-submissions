class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            # this checks if the value diff exists and that the index is not the current index
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        
        return []