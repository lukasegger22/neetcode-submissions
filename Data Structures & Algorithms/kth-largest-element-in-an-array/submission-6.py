class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for number in nums:
            
            if len(min_heap) < k:
                heapq.heappush(min_heap, number)
            else:
                if number > min_heap[0]:
                    heapq.heappushpop(min_heap, number)
        return min_heap[0]