class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            diff = target - n
            # check if complement exists in the map
            if diff in indices:
                # return the complement and current index
                return [indices[diff], i]
            # if not, add the value to the index
            indices[n] = i

# nums = [2, 7, 11, 15]
# target = 9
# i=0, n=2, diff = 7, check if 7 is in indices
    # 7 not in indices so indices stores 2 -> 0

# then for 9-7 = 2, check if 2 is in indices
# indices[diff] stores index 0, i is the current index so that is how it gets returned
