class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.insert(word)
        
        res = set()
        row = len(board)
        col = len(board[0])
        
        
        def dfs(r, c, node, word):
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            
            char = board[r][c] 

            if char not in node.children:
                return 
            
            node = node.children[char]
            word += char

            if node.endOfWord:
                res.add(word)
            
            board[r][c] = "#"

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            board[r][c] = char
        
        for r in range(row):
            for c in range(col):
                dfs(r,c, trie, "")
        return list(res)
        