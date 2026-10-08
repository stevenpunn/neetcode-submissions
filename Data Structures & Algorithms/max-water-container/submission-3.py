class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            # area = shorter height of the two bars * width
            # min heights to find the shorter of the two bars
            # (right - left) subtracts indices (width)
            area = min(heights[left], heights[right]) * (right - left)
            # result we store is the max of current result or the area we just calculated
            result = max(result, area)

            # move the pointer at the shorter height
            # this helps find the larger height to calculate area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result