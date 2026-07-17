class Solution {
    public boolean isPalindrome(String s) {
        if(s.length() <= 1){
            return true;
        }
        int left = 0;
        int right = s.length()-1;
        while(left <= right){
            while(left < right && !Character.isLetterOrDigit(s.charAt(left))){
                left++;
            }
            while(left < right && !Character.isLetterOrDigit(s.charAt(right))){
                right--;
            }
            Character faulterA = Character.toUpperCase(s.charAt(left));
            Character faulterB = Character.toUpperCase(s.charAt(right));
            if(faulterA != faulterB){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
