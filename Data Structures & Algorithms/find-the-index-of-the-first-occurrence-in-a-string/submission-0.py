class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        n = len(haystack)
        m = len(needle)
        for i in range(n):
            j = i
            count = 0
            t = 0

            while j < n and t < m and  haystack[j] == needle[t]:
                j +=1
                t+=1
                count +=1
            if count == m:
                return i
        return -1
