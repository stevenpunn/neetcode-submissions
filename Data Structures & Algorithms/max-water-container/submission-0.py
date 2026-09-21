class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initialize left ptr at the beginning, right ptr at the end
        l = 0
        r = len(heights) - 1
        res = 0
        # while left ptr is less than right ptr
        while l < r:
            # area = min height * the width b/w indicies (r-l)
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)    # res = max of our current res, or the new area
            if heights[l] <= heights[r]:
                l += 1  # move the left index inward by 1 
            else:
                r -= 1  # move the right index inward by 1
        return res