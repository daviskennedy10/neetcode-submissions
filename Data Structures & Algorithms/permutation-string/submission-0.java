class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length() > s2.length()){
            return false;
        }
        HashMap<Character, Integer> s1Count = new HashMap<>();
        for(char c : s1.toCharArray()){
            s1Count.put(c, s1Count.getOrDefault(c, 0) + 1);
        }
        int l = 0;
        HashMap<Character, Integer> window = new HashMap<>();
        int windowL = s1.length();
        for(int r = 0; r < s2.length(); r++){
            window.put(s2.charAt(r), window.getOrDefault(s2.charAt(r), 0) + 1);
            if(r - l + 1 > windowL){
                window.put(s2.charAt(l), window.get(s2.charAt(l)) - 1);
                if(window.get(s2.charAt(l)) == 0){
                    window.remove(s2.charAt(l));
                }
                l++;
            }
            if(window.equals(s1Count)){
                return true;
            }

        }
        return false;
        
    }
}