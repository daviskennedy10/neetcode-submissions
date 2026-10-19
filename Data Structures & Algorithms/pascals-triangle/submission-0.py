class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        count = 1
        while count <= numRows:
            ans = [1] * count
            if count >= 3:
                ans = []
                # ans = [1] + ans + [1]
                prev = res[-1]
                for i in range(len(prev)-1):
                    ans.append(prev[i]+prev[i+1])
                ans = [1] + ans + [1]
            
            res.append(ans)
            count +=1
        return res