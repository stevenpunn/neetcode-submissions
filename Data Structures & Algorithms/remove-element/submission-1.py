class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # the first idea is to use 2 pointers that requires a temporary storage
        # pointer k stores the next valid element should go
        # 2 pointer approach where i reads and k writes
        k = 0
        for i in range(len(nums)):
            # if nums[i] != val, copy it to nums[k] and increment k
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        # k = count of valid elements
        return k

'''
given nums [3, 2, 2, 3], val = 3
when i = 0, we skip
when i = 1, we see 2 so at nums[0], set it to k=1
when i = 2, we see 2, so at nums[1], set k=2
when i = 3, we skip

'''