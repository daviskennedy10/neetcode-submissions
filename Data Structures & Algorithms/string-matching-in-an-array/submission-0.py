class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        n = len(words)
        for i in range(n):
            count = 0
            for j in range(n):
                if words[i] in words[j]:
                    count +=1

            if count > 1:
                res.append(words[i])
        return res