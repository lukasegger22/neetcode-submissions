class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for char in tasks:
            count[char] = count.get(char,0)+1
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                val = heapq.heappop(max_heap)
                val += 1  
                if val < 0:
                    q.append([val, time + n])
            if q and q[0][1] == time:
                bereit_element = q.popleft()
                heapq.heappush(max_heap, bereit_element[0])
                
        return time

