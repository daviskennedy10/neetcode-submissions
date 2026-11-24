class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mapper = Counter(s)
        n = len(s)
        longest = -1
        length = 0
        check = set()
        for i in range(n):
            if s[i] in check:
                continue
            if mapper[s[i]] > 1:
                j = i+1
                length = 0
                count = 0
                highest = mapper[s[i]] - 1
                while j < n and count < highest:
                    length+=1
                    if s[j] == s[i]:
                        count +=1
                    if s[j] == s[i] and count == highest:
                        length-=1
                    j+=1
                longest = max(longest, length)
            check.add(s[i])
        return longest
