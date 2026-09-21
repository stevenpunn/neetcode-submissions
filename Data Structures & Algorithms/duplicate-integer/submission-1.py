class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate through the array, use 2 pointers
        ''' O(n^2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False
        '''
        # using hashset to store unique elements
        list_nums = set()

        for i in range(len(nums)):
            if nums[i] in list_nums:
                 return True
            list_nums.add(nums[i])
        return False