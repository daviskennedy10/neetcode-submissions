class Solution {
    Map<Character, String> map;
    List<String> res;
    String combo;
    public List<String> letterCombinations(String digits) {
        map = new HashMap<>();
        res = new ArrayList<>();
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");
        if(digits.isEmpty()){
            return res;
        }
        combo = "";
        dfs(digits, 0, combo);
        return res;
    }

    private void dfs(String digits, int i, String combo){
        if(combo.length() == digits.length()){
            res.add(combo);
            return;
        }
        Character number = digits.charAt(i);
        String associates = map.get(number);
        for(int j = 0; j < associates.length(); j++){
            dfs(digits, i+1, combo+ associates.charAt(j));
        }

    }
}
