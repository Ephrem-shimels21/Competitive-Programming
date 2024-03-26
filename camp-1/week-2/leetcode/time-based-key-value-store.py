class TimeMap:

    def __init__(self):
        self.TimeMap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap[key].append((timestamp, value))
    
    def get(self, key: str, timestamp: int) -> str:
        candidates = self.TimeMap[key]
        if not candidates:
            return ""
        l = 0
        r = len(candidates) - 1
        max_prev = [float('-inf'), ""]

        while l <= r:
            mid = (l + r) // 2
            time, value = candidates[mid]
            if time == timestamp:
                return value
            
            elif time < timestamp:
                if time > max_prev[0]:
                    max_prev[0] = time
                    max_prev[1] = value
                l = mid + 1
            
            elif time > timestamp:
                r = mid - 1

        return max_prev[1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)