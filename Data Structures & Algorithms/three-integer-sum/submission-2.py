class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we can fix one number and search for the other 2 numbers
        # this is so that we can skip duplicates
        # array to store the result
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # set breakpoint, if a > 0 then the remaining nums are positive
            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue
            # set 2 pointers, left = pointer left of a
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                # threeSum > 0, value too high so move right pointer inwards
                if threeSum > 0:
                    right -= 1
                # threeSum < 0, value too low so increase left
                elif threeSum < 0:
                    left += 1
                # if threeSum == 0: 
                else:
                    # add the triplet to the result
                    res.append([a, nums[left], nums[right]])
                    # move both pointers inwards
                    left += 1
                    right -= 1
                    # skip duplicates at the left pointer
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res

        