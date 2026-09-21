class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hashmap that maps numbers to their 1-indexed positions
        mp = defaultdict(int)

        # loop through array with index i from 0 to n-1
        for i in range(len(numbers)):
            # compute complement
            temp = target - numbers[i]

            # if temp exists in mp, return the index
            if mp[temp]:
                return [mp[temp], i+1]
            # otherwise, store the current number in the map
            mp[numbers[i]] = i + 1
        return []
