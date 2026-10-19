class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            ans = [1] * (i+1)
            if i >= 2:
                ans = []
                prev = res[-1]
                for j in range(len(prev)-1):
                    ans.append(prev[j]+prev[j+1])
                ans = [1] + ans + [1]
            
            res.append(ans)
        return res