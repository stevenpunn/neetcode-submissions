class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using a hashset
        indices = {}

        # iterate and sotre the value and index of each index
        for i, n in enumerate(nums):
            indices[n] = i  # assign the value of the index to an index

        # iterate through the value and index of each element
        for i, n in enumerate(nums):
            diff = target - n   # calculate the difference in target vs current index val
            # if difference in indices and index of the diff is not the current index
            if diff in indices and indices[diff] != i:  
                return [i, indices[diff]]       # return current index, index of the diff

        return []
            