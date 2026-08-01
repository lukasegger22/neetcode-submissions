class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        min_heap = []
        for char in tasks:
            count[char] = count.get(char,0)+1
        for char in count:
            heapq.heappush(min_heap, (-count[char], char))
        queue = deque()
        time = 0
        while len(min_heap) > 0 or len(queue) > 0:
            if len(min_heap) > 0:
                tupel = heapq.heappop(min_heap)
                val = -tupel[0]
                char = tupel[1]
                if val-1 > 0:
                    queue.append((-(val-1),char,n+time))
            print(queue)
            if len(queue) > 0 and queue[0][2] == time:
                values = queue.popleft()
                if -values[0]> 0:
                    heapq.heappush(min_heap, (values[0], values[1]))
            time+=1
        return time