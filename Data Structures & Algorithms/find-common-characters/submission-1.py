class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        final = []
        n = len(words)
        use = words[0]
        
        for char in use:
            count = 0
            for j in range(n):
                if char in words[j]:
                    count += 1
                    words[j] = words[j].replace(char, "", 1)
            if count == n:
                final.append(char)
                
        return final