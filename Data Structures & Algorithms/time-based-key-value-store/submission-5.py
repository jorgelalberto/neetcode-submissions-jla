from collections import defaultdict as dd
class TimeMap:

    def __init__(self):
        self.timeMaps = dd(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMaps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.timeMaps) or (timestamp < self.timeMaps[key][0][0]):
            return ""
        timeMap = self.timeMaps[key]

        l = 0
        r = len(timeMap)-1
        max_ind = 0
        while l<=r:
            mid = (l+r)//2
            if timeMap[mid][0] == timestamp:
                return timeMap[mid][1]
            elif timeMap[mid][0] < timestamp:
                max_ind = max(max_ind, mid)
                l = mid + 1
            else:
                r = mid - 1

        return timeMap[max_ind][1]
