class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # the 2 values must be the same
        # the difference between indices must be <= k
        # so we are check if indices are at most k indices apart

        # we can use a hashmap to store the most recent index it appeared
        myMap = {}
        for i in range(len(nums)):
            # first we check if nums[i] is in myMap (have we seen before)
            # then check i - myMap[nums[i]] <= k if it is close enough
            if nums[i] in myMap and i - myMap[nums[i]] <= k:
                # if yes, return True
                return True
            # record or update latest index for this number
            myMap[nums[i]] = i
    
        return False