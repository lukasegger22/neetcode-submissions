class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for val in points:
            calc = ( (val[0])**2 + val[1]**2 )
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-calc, val))
            else:
                heapq.heappushpop(max_heap, (-calc, val))
        return [point for dis, point in max_heap]
