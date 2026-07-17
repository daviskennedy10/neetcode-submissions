class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int l = 0;
        boolean ans = false;
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < s1.length(); i++){
            map.put(s1.charAt(i), map.getOrDefault(s1.charAt(i), 0)+ 1);
        }
        Map<Character, Integer> mapB = new HashMap<>();
        for(int r = 0; r < s2.length(); r++){
            mapB.put(s2.charAt(r), mapB.getOrDefault(s2.charAt(r), 0)+ 1);
            
            if(r-l+1 > s1.length()){
                mapB.put(s2.charAt(l), mapB.getOrDefault(s2.charAt(l), 0)- 1);
                if(mapB.get(s2.charAt(l)) == 0){
                    mapB.remove(s2.charAt(l));
                }
                l++;
            }
            if(mapB.equals(map)){
                return true;
            }

        }
        return false;
    }
}
