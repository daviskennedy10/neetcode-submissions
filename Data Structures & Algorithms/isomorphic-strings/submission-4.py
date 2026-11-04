class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cache = {}
        faster = set()
        n = len(t)
        res = ""
        for i in range(n):
            if s[i] in cache:
                if cache[s[i]] != t[i]:
                    return False
            else:
                if t[i] in faster:
                    return False
                cache[s[i]] = t[i]
                faster.add(t[i])
        return True
