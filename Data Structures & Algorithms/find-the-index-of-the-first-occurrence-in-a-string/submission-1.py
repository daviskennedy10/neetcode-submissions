class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if needle not in haystack:
            return -1
        
        for i in range(n):
            idx = i
            print(haystack[i:i+m])
            if haystack[i:i+m] == needle:
                return i
        return -1