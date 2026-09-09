class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        count = 0

        def isPali(word,l,r):
            while l < r:
                if word[l] != word[r]:
                    return False
                l +=1
                r -=1
            return True

        while l < r:
            print(s[r])
            print(s[l])
            print(l)
            print(r)
            if s[l] != s[r]:
                if count == 0:
                    count +=1
                    if isPali(s,l+1,r) or isPali(s,l,r-1) :
                        return True
                    else:
                        return False
                else:
                    return False
            l+=1
            r-=1
        return True
        
        
