class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        # iterate the entire list, for each index, compute the difference
        for i, n in enumerate(nums):
            diff = target - n
            # if diff already exists, the pair is found, the earlier index is in the list
            # if not, store the index and value and move on
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

# nums = [2, 7, 11, 15], target = 9
# i=0, n=2, diff=7, prevMap contains nothing so store value 2 at index 0
# i=1, n=7, diff=2, the prevMap contains 2
# so it returns the index of the diff in prevMap and our current index (i)