class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # nums become our minheap
        self.minHeap, self.k = nums, k
        # heapify converts our list into a min heap
        heapq.heapify(self.minHeap)
        # reduce the heap to size k, if there are more than k numbers, remove the smallest one
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # push the new value into the heap
        heapq.heappush(self.minHeap, val)
        # we only keep k elements
        # if the heap size > k, remove the smallest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            # because this is a min-heap, the smallest element is the k-th largest # overall
        return self.minHeap[0]
