class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        s_map = {}
        letter_max = 0
        l=0
        for r in range(len(s)):
            s_map[s[r]] = s_map.get(s[r], 0) + 1
            letter_max = max(letter_max, s_map.get(s[r]) )

            while (r - l+1) - letter_max > k:
                put = s_map.get(s[l])
                if put == 1:
                    del s_map[s[l]]
                else:
                    s_map[s[l]] = put - 1
                l+=1
            longest =  max(longest, r-l+1)

        return longest


