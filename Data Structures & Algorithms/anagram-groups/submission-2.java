class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        List<List<String>> result = new ArrayList<>();
        for(int i = 0; i < strs.length; i++){
            char[] word = strs[i].toCharArray();
            Arrays.sort(word);
            String anagram = new String(word);
            map.computeIfAbsent(anagram, k -> new ArrayList()).add(strs[i]);
        }
        for(List<String> element : map.values()){
            result.add(element);
        }
        return result;


    }
}
