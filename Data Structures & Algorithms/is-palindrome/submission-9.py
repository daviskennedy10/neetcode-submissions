class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        l = 0
        r = len(t) - 1
        while l < r :
            while  l < r and not t[r].isalnum():
                r-=1
            while l < r and not t[l].isalnum():
                l+=1

            if t[r] == t[l]:
                r-=1
                l+=1
            else:
                return False
        return True