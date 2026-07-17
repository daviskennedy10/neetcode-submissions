class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        max_f = 0
        word_map = {}

        for r in range(len(s)):
            word_map[s[r]] = word_map.get(s[r], 0) + 1
            max_f = max(max_f, word_map.get(s[r]))

            while r-l+1 - max_f > k:
                put = word_map.get(s[l]) - 1
                if put == 0:
                    del word_map[s[l]]
                else:
                    word_map[s[l]] = put

                l +=1

            max_len = max(r-l+1, max_len)
        return max_len
