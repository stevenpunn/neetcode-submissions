class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using hashset to store unique elements
        list_nums = set()

        for i in range(len(nums)):
            if nums[i] in list_nums:
                 return True
            list_nums.add(nums[i])
        return False