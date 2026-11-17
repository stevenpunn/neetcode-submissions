class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use a hashmap to store the frequency of each number
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, ctr in count.items():
            arr.append([ctr, num])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result