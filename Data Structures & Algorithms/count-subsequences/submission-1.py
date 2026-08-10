class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        count = 0
        memo = {}

        def dfs(i, word):
            if word == t:
                return 1
            if (i,word) in memo:
                return memo[(i,word)]
            if i >= len(s):
                return 0
            take = dfs(i+1, word + s[i])
            skip = dfs(i+1, word)
            memo[(i, word)] = take + skip
            return take + skip
        
        return dfs(0, "")