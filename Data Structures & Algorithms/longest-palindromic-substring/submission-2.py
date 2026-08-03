class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPali(l,r):
            res_string = ""
            while l >= 0 and r < len(s) and s[r] == s[l]:
                res_string = s[l:r+1]
                r +=1
                l -=1
            return res_string
        
        n = len(s)
        global_res = ""
        resLen = 0
        for i in range(n):
            resA = isPali(i,i)
            resB = isPali(i,i+1)
            if len(resA) > len(resB):
                curr_res = resA
            else:
                curr_res = resB
            if len(curr_res) > len(global_res):
                global_res = curr_res
            
                
        return global_res
                    