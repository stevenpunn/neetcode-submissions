class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize left pointer at the beginning, right at the end
        left = 0
        right = len(numbers) - 1

        # iterate through the array
        while left < right:
            currSum = numbers[left] + numbers[right] # current sum = left pointer + right pointer val
            # if the sum is larger than the target, right pointer needs to move inward
            if currSum > target:
                right -= 1 

            # if the current sum is smaller than target, move the left pointer to make the sum bigger
            elif currSum < target:
                left += 1
            # if target found, return indices + 1 for 1-based indexing
            else:
                return [left+1, right+1]
        else:
            return []