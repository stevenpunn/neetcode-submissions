class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n)
        l = 0       # start of the array
        r = len(numbers) - 1    # end of the array

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l +=1
            else:
                return [l+1, r+1]
        
        return []