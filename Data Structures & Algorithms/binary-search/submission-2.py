class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # goal is to run in O(logn)
        # compute this iteratively
        # want to split the array in half then search left and right half
        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = left + ((right - left) // 2)  # mid = (l+r) // 2 can lead to overflow

            if nums[mid] > target:      # target higher than middle
                right = mid - 1         # move the right pointer to the left half, search there
            elif nums[mid] < target:    # target is lower than the middle
                left = mid + 1          # move the left pointer to the right half
            else:
                return mid              # otherwise return the middle
        return -1               # return -1 if nothing was found