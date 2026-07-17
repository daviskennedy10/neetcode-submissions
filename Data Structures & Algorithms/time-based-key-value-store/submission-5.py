class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = self.store.get(key)
        check = 0
        ans = ""
        if res is None:
            return ans
        else:
            l,r = 0, len(res)-1
            while l<=r:
                mid = (l+r)//2
                if res[mid][0] == timestamp:
                    return res[mid][1]
                elif res[mid][0] > timestamp:
                    r = mid - 1
                else:
                    ans = res[mid][1]
                    l = mid + 1
        return ans
