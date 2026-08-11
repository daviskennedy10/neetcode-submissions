class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n = len(word1)
        m = len(word2)
        #count = 0
        #i, j = 0,0
        #while i < n and j < m:
            #if word1[i] == word2[j]:
             #   i+=1
             #   j+=1
           # else:
           #     count +=1
            #    i += 1 # delete

            #    count += 1
            #    i +=1
            #    j +=1 #change number

            #    count += 1
            #    j +=1 # insert
                
        #while j >= m and i < n:
        #    count +=1
        #    i +=1
        #while i >= m and j < m:
          #  count +=1
         #   j +=1
        #return count


        memo = {}
        def dfs(i,j):
            if i >= n and j >= m:
                return 0
            if i >= n and j < m:
                return m - j
            if j >= m and i < n:
                return n - i
            if (i,j) in memo:
                return memo[(i,j)]
            
            if word1[i] == word2[j]:
                memo[(i,j)] = dfs(i+1,j+1)
                return memo[(i,j)]
            
            else:
                remove = 1 + dfs(i+1,j)
                change = 1 + dfs(i+1,j+1)
                insert = 1 + dfs(i,j+1)
                memo[(i,j)] = min(remove,change, insert)
                return memo[(i,j)]
            
        return dfs(0,0)
            