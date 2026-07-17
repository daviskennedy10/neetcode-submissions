class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        l = 0
        t_count, s_count ={},{}
        res = [-1,-1]
        resLen = float("infinity")

        t_count = Counter(t)
        have, need = 0, len(t_count)

        for r in range(len(s)):
            s_count[s[r]] = s_count.get(s[r],0) + 1
            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                have +=1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                s_count[s[l]] -=1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have-=1
                
                l+=1
        l,r = res
        return s[l: r+1] if resLen < float("infinity") else ""