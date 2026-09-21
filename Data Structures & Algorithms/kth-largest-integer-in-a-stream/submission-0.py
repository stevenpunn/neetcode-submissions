class KthLargest:
    # using min heaps

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k      # initialize all numbers into min-heap
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:        # if the heap size is > k, remove the smallest element
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)   # insert the new value into the minheap
        if len(self.minHeap) > self.k:      # if heap size > k, remove the smallest element (heap root)
            heapq.heappop(self.minHeap)
        return self.minHeap[0]               # return heap's smallest element (root), now k-th largest
