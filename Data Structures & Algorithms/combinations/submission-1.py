class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def dfs(i,ans):
            if len(ans) == k:
                res.append(ans[:])
                return
            if len(ans) > k or i > n:
                return

            ans.append(i)
            dfs(i+1,ans)
            ans.pop()
            dfs(i+1,ans) 
        dfs(1,[])
        return res
    