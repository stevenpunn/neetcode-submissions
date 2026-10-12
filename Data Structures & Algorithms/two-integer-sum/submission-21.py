class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hash map 1 pass through
        prevMap = {}    # assigns value to index

        # iterate through the array using index i 
        for i, n in enumerate(nums):
            diff = target - n
            # check if the complement exists in the hashmap
            if diff in prevMap:
                # return the indices of the current element and its complement
                return [prevMap[diff], i]
            prevMap[n] = i