class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        def isPali(l,r,word):       
            while l >= 0 and r < n:
                if word[r] != word[l]:
                    return s[l+1:r]
                l-=1
                r+=1
            if l < 0:
                return s[:r]
            elif r >= n:
                return s[l+1:]
            return s[l:r+1]
        
        r,l = n-1, 0
        res = ""
        for i in range(n):
            letter = s[i]
            longest_valid_odd = isPali(i-1,i+1,s)
            longest_valid_even = isPali(i,i+1,s)
            if len(longest_valid_even) > len(longest_valid_odd):
                longest_any = longest_valid_even
            else:
                longest_any = longest_valid_odd
            if len(longest_any) > len(res):
                res = longest_any
        return res

        
        #for loop:
            #add pointer element
           # while the window is invalid -> its not a palindrome and window length < 3:
               # move the l pointer forward
            
            # if length of our window is biggger than current length:
                # our res = s[l:r+1]
        
        #return the string version of res
        # r = b, l=b, window = b, res = b
        # r = a, window ab, res = ab
        # r = b, window = bab res = bab
        # r = a, window baba

        