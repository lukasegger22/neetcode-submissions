class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
    def add(self, val: int) -> int:
        min_heap = self.nums
        heapq.heappush(min_heap,val)
        while len(min_heap) > self.k:
            heapq.heappop(min_heap)
        return min_heap[0]