class Solution:
    def longestPalindrome(self, s: str) -> int:
        use = Counter(s)
        count = 0
        allows = len(s)
        print(use)
        found = False
        for k,v in use.items():
            best = max(v-1, (v//2)*2)
            count += best
            if v % 2 != 0:
                found = True
        if found:
            count += 1
        return count