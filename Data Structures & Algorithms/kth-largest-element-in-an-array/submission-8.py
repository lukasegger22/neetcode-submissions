class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for val in nums[k:]:
            if val > min_heap[0]:
                heapq.heapreplace(min_heap, val)
        return min_heap[0]
            

