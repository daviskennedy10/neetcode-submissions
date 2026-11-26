class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # |AB|AB
        # defining our lengtht for every valid window
        # define our maximum length that we comparre wirh each valid length -> 
        # define our l pointer at 0
        # AABAC. K = 2; A=3,B=1,C=1
        window_map = {}
        length = 0
        maxLen = 0
        n = len(s)
        l = 0
        highest = float("-inf")
        for r in range(n):
            window_map[s[r]] = window_map.get(s[r],0)+1
            highest = max(highest, window_map[s[r]])
            while r-l+1 - highest > k:
                if window_map[s[l]] == 1:
                    del window_map[s[l]]
                else:
                    window_map[s[l]] -=1
                l+=1
            maxLen = max(maxLen, r-l+1)  
            
        return maxLen


