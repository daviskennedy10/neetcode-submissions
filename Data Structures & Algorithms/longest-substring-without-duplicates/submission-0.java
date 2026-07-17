class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> check = new HashSet<>();
        int l = 0;
        int maximum = 0;
        for(int r = 0; r < s.length(); r++){
            while(check.contains(s.charAt(r))){
                check.remove(s.charAt(l));
                l++;

            }
            int wLen = (r - l) + 1;
            maximum = Math.max(wLen, maximum);
            check.add(s.charAt(r));
        }
        return maximum;
    }
}
