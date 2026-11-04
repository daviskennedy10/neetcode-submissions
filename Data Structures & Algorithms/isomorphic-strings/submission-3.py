class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cache = {}
        n = len(t)
        res = ""
        for i in range(n):
            if s[i] in cache:
                res += cache[s[i]]
            else:
                if t[i] in cache.values():
                    return False
                res += t[i]
                cache[s[i]] = t[i]
        return res == t
