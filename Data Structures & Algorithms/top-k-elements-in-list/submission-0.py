class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # aim for O(n)
        # use bucket sort, for each count, store the values that appear that many times
        # use hashmap to count occurrances of each value
        count = {}
        frequency = [[]for i in range(len(nums) + 1)]   # array to track nums

        for n in nums:  # iterate through each value in nums
            count[n] = 1 + count.get(n, 0)  # count how many times each value occurs
        for n, c in count.items():      # go through each value counted
            frequency[c].append(n)      # at index count, append value n, n appears c times

        res = []
        for i in range(len(frequency) - 1, 0, -1):  # iterate in descending order
            for n in frequency[i]:      # go through each n value in freq @ idx i:
                res.append(n)           # append n value to result
                if len(res) == k:       # if result length = k, return result
                    return res
            