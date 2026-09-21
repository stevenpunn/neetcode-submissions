class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using a hash map
        # initialize indices
        indices = {}

        # use enumerate to get index and element at the same time
        for i, n in enumerate(nums):
            indices[n] = i
            
        # iterate through the array
        for i, n in enumerate(nums):
            diff = target - n   # compute the complement of the current element
            if diff in indices and indices[diff] != i:      # if the complement exists
                return [i, indices[diff]]       # return current index and complement
        return []
        