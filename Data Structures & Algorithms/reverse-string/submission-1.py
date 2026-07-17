class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        mid = r/ 2

        while l < mid:
            s[l], s[r] = s[r], s[l]
            l +=1
            r -=1
        return s
