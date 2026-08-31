class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)
        for val in points:
            calc = ( (val[0])**2 + val[1]**2 )**0.5
            heapq.heappush(max_heap, (-calc, val))
            if len(max_heap) >k:
                heapq.heappop(max_heap)
        return [point for dis, point in max_heap]
