class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        heapq.heapify(min_heap)
        for number in nums:
            heapq.heappush(min_heap, number)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]