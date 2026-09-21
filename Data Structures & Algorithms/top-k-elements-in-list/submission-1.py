class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using min-heap
        # build a frequency map that counts how many times each number appears
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # create an empty min-heap
        heap = []
        # for each number in the frequency map:
        for num in count.keys():
            heapq.heappush(heap, (count[num], num)) # push (frequency, number) into the heap
            if len(heap) > k:   # if heap size > k
                heapq.heappop(heap) # pop once to remove smallest frequency

        # heap now conatins the k more frequent elements
        res = []
        # pop all elements from the heap and collect their nums into result list
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res