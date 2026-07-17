class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        Set<Character> set = new HashSet<>();
        int longest = 0;
        for(int r = 0; r < s.length(); r++){
            while(set.contains(s.charAt(r)) && l < r){
                set.remove(s.charAt(l));
                l++;
            }
            int size = r - l + 1;
            longest = Math.max(size, longest);
            set.add(s.charAt(r));
        }
        return longest;
    }
}
