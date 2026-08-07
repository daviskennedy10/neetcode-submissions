class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """if len(text1) < len(text2):
            small, big = text1, text2
        else:
            small, big = text2, text1
    
        
        def dfs(i,j):
            if i >= len(small) or j >= len(big):
                return 
            if small[i] == big[j]:
                count[0] +=1
                1 + dfs(i+1,j+1)
            else:
                count[0] = max(dfs(i,j+1, count),dfs(i+1,j, count)) 
            return count[0]
                    

        
        
        return dfs(0,0,[0])
        """

        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]