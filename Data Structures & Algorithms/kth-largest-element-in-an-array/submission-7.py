class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for val in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, val)
            else:
                heapq.heappushpop(min_heap, val)
        return min_heap[0]
            

