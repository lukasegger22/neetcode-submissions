class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)
        for point in points:
            x = point[0]
            y = point[1]
            distance = -( x**2 + y**2)
            heapq.heappush(min_heap, (distance,[x,y]))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [point for distance, point in min_heap]