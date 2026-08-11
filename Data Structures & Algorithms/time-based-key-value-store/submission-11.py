class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        res = ""
        left = 0
        right = len(self.timemap[key])-1
        while left <= right:
            mid = (left+right)//2
            if timestamp == self.timemap[key][mid][1]:
                res = self.timemap[key][mid][0]
                break
            elif timestamp > self.timemap[key][mid][1]:
                res = self.timemap[key][mid][0]
                left = mid+1
            else:
                right = mid-1
        return res

