class TrieNode{
    TrieNode[] children = new TrieNode[26];
    boolean endOfWord = false;
}
class WordDictionary {
    TrieNode root;

    public WordDictionary() {
        root = new TrieNode();


    }

    public void addWord(String word) {
        TrieNode curr = root;
        for(char c : word.toCharArray()){
            int i = c - 'a';
            if(curr.children[i] == null){
                curr.children[i] = new TrieNode();
            }
            curr = curr.children[i];
        }
        curr.endOfWord = true;

    }

    public boolean search(String word) {
        return dfs(0, root, word);

    }
    private boolean dfs(int j, TrieNode root, String word){
        TrieNode curr = root;
        for(int i = j; i < word.length(); i++){
            if(word.charAt(i) == '.'){
                for(TrieNode child : curr.children){
                    if(child != null && dfs(i+1, child, word)){
                        return true;
                    }
                }
                return false;
            }
            else{
                int p = word.charAt(i) - 'a';
                if(curr.children[p] == null){
                    return false;
                }
                curr = curr.children[p];
            }
            
        }
        return curr.endOfWord;



    }
}
