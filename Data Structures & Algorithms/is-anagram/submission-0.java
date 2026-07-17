class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!= t.length()){
            return false;
        }
        char[] son = s.toCharArray();
        char[] top = t.toCharArray();
        Arrays.sort(son);
        Arrays.sort(top);
        for(int i = 0; i < Math.min(son.length, top.length); i++){
            if(son[i] != top[i]){
                return false;
            }

        }
        return true;

    }
}
