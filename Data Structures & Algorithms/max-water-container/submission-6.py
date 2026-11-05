class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0

        while left <= right:
            # calculate the area, and store highest area found so far
            area = min(heights[left], heights[right]) * (right - left)
            result = max(area, result)

            # continue to walk through the entire list
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return result