class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            if x > y:
                new_val = x - y
                heapq.heappush(max_heap, -new_val)
            elif y > x:
                new_val = y-x
                heapq.heappush(max_heap, -new_val)
            else:
                heapq.heappush(max_heap, 0)
        return -max_heap[0]

        

        