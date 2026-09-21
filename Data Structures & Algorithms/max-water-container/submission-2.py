class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            # the area is limited by the height of the shorter bar
            # we multiply this by the width (right index - left index)
            area = min(heights[left], heights[right]) * (right-left)
            # we update result with  the maximum area found so far
            result = max(result, area)

            # move the pointer at the shorter height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result

# in this problem, we will check all points, and update when we find a max