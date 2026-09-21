class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using hashset to store unique elements
        list_nums = set()

        # iterate through the hash set
        for i in range(len(nums)):
            # if our number is in the list, return true
            if nums[i] in list_nums:
                 return True
            else:
                # add the number to the list otherwise
                list_nums.add(nums[i])
        # if the loop finishes without finding duplicate, return false
        return False