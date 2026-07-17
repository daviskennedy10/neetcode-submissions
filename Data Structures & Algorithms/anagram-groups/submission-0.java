class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
       Map<String, ArrayList<String>> container = new HashMap<>();
       for(String word : strs){
        char[] leg = word.toCharArray();
        Arrays.sort(leg);
        String raw = new String(leg);
        if(!container.containsKey(raw)){
            container.put(raw, new ArrayList<>());
        }
        container.get(raw).add(word);

       } 
       return new ArrayList<>(container.values());
    }
}
