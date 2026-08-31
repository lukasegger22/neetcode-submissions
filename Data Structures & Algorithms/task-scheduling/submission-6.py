class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for char in tasks:
            count[char] = count.get(char,0)+1
        max_heap = []
        for char in count:
            heapq.heappush(max_heap, (-count[char], char))
        queue = deque()
        time = 0
        while queue or max_heap:
            if len(max_heap) > 0:
                val = heapq.heappop(max_heap)
                if val[0] != -1:
                    queue.append((val[0]+1, val[1], n + time))
            if len(queue) > 0 and queue[0][2] == time:
                q_val = queue.popleft()
                heapq.heappush(max_heap, (q_val[0],q_val[1]))
            time+=1
        return time
        
            