class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapper = Counter(s)
        n = len(s)

        print(mapper)
        check = set()
        for i in range(n):
            if mapper[s[i]] == 1:
                return i
        return -1

