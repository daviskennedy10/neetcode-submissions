class Solution {
    public int lengthOfLongestSubstring(String s) {
      int l = 0;
      int length = 0;
      int maxLength = 0;
      Set<Character> set = new HashSet<>();

      for(int r = 0; r < s.length(); r++){
        while(set.contains(s.charAt(r)) && r > l){
            set.remove(s.charAt(l));
            l++;

        }
        int size = r - l + 1;
        maxLength = Math.max(maxLength, size);
        set.add(s.charAt(r));
      }
      return maxLength;
    }
}
