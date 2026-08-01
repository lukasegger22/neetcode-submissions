class TimeMap:

    def __init__(self):
       self.count = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.count:
            self.count[key] =[]
        self.count[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.count:
            return ""
        res = ""
        werte_liste = self.count[key]
        left = 0
        right = len(werte_liste)-1
        while left <= right:
            mid = (left+right)//2
            mid_time = werte_liste[mid][1]
            if timestamp == werte_liste[mid][1]:
                return werte_liste[mid][0]
            elif timestamp > werte_liste[mid][1]:
                res = werte_liste[mid][0]
                left = mid+1
            else:
                right = mid-1
        return res