class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        ArrayList<List<String>> result = new ArrayList<>();
        Map<String, ArrayList<String>> placer = new HashMap<>();
        for(int i = 0; i < strs.length; i++){
            char[] word = strs[i].toCharArray();
            Arrays.sort(word);
            String anagram = new String(word);
            placer.computeIfAbsent(anagram, k -> new ArrayList<>()).add(strs[i]);

        }
        for(ArrayList<String> c : placer.values()){
            result.add(c);
        }
        return result;
    }
}
