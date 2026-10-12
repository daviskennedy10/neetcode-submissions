class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        j = 0
        if len(t) < n:
            return False
        for i in range(n):
            if j < len(t) and s[i] == t[j]:
                j +=1
                continue
            else:
                while j < len(t) and s[i] != t[j]:
                    j +=1
                if j >= len(t):
                    return False
                j+=1
        return True
