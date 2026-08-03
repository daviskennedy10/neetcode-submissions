class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def isPali(l,r):
            nonlocal count
            while l >= 0 and r < len(s) and s[r] == s[l]:
        
                count += 1
                r +=1
                l -=1
            return 
        
        n = len(s)
       
        for i in range(n):
            isPali(i,i)
            isPali(i,i+1)

            
                
        return count