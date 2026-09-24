class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # the first idea is to use 2 pointers that requires a temporary storage
        # we can circumvent this by removing vals in place
        # pointer k stores the next valid element should go
        k = 0
        for i in range(len(nums)):
            # if nums[i] != val, copy it to nums[k] and increment k
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        # k = count of valid elements
        return k