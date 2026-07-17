class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=[]
        strs.sort()
        last = strs[-1]
        first = strs[0]
        i=0
        while i < len(last):
            if i >= len(first):
                break
            if first[i] == last[i]:
                res.append(first[i])
                
            else:
                break
            i+=1
        ans = "".join(res)
        return ans
