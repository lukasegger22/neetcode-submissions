class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x,y in points:
            euklid = (x**2 + y**2)
            heapq.heappush(max_heap, (-euklid, [x,y]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [point[1] for point in max_heap ]