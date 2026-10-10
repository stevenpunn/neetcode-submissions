class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # must find the minimum eating rate to eat all bananas within h hours
        # use a binary search approach
        # rather than checking each speed one by one,set a range 
        
        left = 1        # minimum possible speed
        right = max(piles)  # maximum needed speed
        result = right

        while left <= right:
            # k = middle which is the current speed to test
            k = (left+right) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        return result