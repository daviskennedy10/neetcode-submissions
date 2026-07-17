class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_map = {}

        for i in range(len(s1)):
            s1_map[s1[i]] = s1_map.get(s1[i], 0)+1
        
        s2_map = {}

        for r in range(len(s2)):
            while r-l+1 > len(s1):
                put = s2_map.get(s2[l])
                if put == 1:
                    del s2_map[s2[l]]
                else:
                    s2_map[s2[l]] = put - 1
                l+=1
            
            
            s2_map[s2[r]] = s2_map.get(s2[r], 0)+1
            if s2_map == s1_map:
                return True
        
        return False
