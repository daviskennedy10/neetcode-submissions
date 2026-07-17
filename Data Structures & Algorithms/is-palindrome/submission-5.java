class Solution {
    public boolean isPalindrome(String s) {
        if(s.length() <= 1){
            return true;
        }
        String sentence = s.toUpperCase();
        int left = 0;
        int right = sentence.length() - 1;
        while(left <= right){
            while(!Character.isLetterOrDigit(sentence.charAt(left)) && left < right){
                left++;
            }
            while(!Character.isLetterOrDigit(sentence.charAt(right)) && left < right){
                right--;
            }
            if(sentence.charAt(left) != sentence.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
