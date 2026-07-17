class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        length = 0
        l = 0
        check = set()

        for r in range(len(s)):
            while s[r] in check and l < r:
                check.remove(s[l])
                l +=1
            length = r-l+1
            max_length= max(max_length, length) 
            check.add(s[r])  
        return max_length
                




