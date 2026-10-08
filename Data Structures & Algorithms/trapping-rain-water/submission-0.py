class Solution:
    def trap(self, height: List[int]) -> int:
        # water container depends on the shorter of the two walls
        # start with 2 pointers at the front and end, track the max of the tallest walls seen

        if not height:
            return 0

        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        result = 0

        while left < right:
        # keep track of the highest wall seen so far 
        # water at each position = max wall on that side - height at that position
            if leftMax < rightMax:
                left += 1   # move left pointer inwards
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]

        return result
            