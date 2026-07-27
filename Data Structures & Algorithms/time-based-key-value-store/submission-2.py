class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        historie = self.store[key]
        result = ""
        left = 0 
        right = len(historie)-1
        while left <= right:
            mid = (left+right)//2
            mid_val = historie[mid][0]
            mid_time = historie[mid][1]
            if timestamp == mid_time:
                return mid_val
            elif timestamp > mid_time:
                result = mid_val
                left=mid+1
            else:
                right=mid-1
        return result