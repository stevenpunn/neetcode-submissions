class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # first we can build a minheap, convert every x to -x
        # from this, we can use heappop to remove the smallest element (really, the largest)
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:      # when there is atleast more than 1 stone:
            first = heapq.heappop(stones)       # pop the two heaviest stones
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)      # push diff back into the heap

        stones.append(0)        # if heap is empty, return 0
        return abs(stones[0])   # return abs. value of the remaining stone