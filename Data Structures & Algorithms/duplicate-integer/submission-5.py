class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize a hash set 
        # hashsets are unordered, but do NOT allow duplicates
        found = set()

        # iterate through the nums array
        for num in nums:    
            if num in found:    # if it was found, return True
                return True
            else:
                found.add(num)  # else, add it to the hashset
        return False    # if not found at all, return False
        