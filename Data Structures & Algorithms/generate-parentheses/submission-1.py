class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def dfs(num_open, num_close):
            if num_open == num_close == n:
                res.append("".join(subset))
                return
            if num_open > num_close:
                subset.append(")")
                dfs(num_open, num_close+1)
                subset.pop()
            if num_open < n:
                subset.append("(")
                dfs(num_open+1, num_close)
                subset.pop()
            

        dfs(0, 0)
        return res