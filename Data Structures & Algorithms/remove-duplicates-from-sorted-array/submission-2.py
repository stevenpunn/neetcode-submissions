class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # we can compare elements to its predecessor
        left = 1    # left will always be unique
        
        # iterate right from 1 to the end
        for right in range(1, len(nums)):
            # if the right pointer differs from the predecessor, it is unqie
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]    # copy the position of right to the left position
                left += 1   # increment left as the count to the unique element
        return left
