class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
       # add = 0
       # for j in range(len(wordDict)):
            #if j > 0:
            #    add = len(wordDict[j-1])
           # for i, c in enumerate(wordDict[j]):
             #   idx = i + add
             #   if c != s[idx]:
              #      return False
        #return True

        
        visited = set()
        def dfs(word):
            if word == "":
                return True
            if word in visited:
                return
            visited.add(word)
            for opt in wordDict:
                if word.startswith(opt):
                    next_word = word[len(opt):]
                    if dfs(next_word):
                        return True
            return False
        
        return dfs(s)

    