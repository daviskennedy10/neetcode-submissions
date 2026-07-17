class Solution {
    public boolean isValid(String s) {
        Map<Character, Character > container = new HashMap<>();
        Stack<Character> stack = new Stack<>();
        if(s.length() % 2 != 0){
            return false;
        }
        container.put(')', '(');
        container.put('}', '{');
        container.put(']', '[');
        char[] arr = s.toCharArray();
        for(int i = 0; i < arr.length; i++){
            if(container.containsValue(arr[i])){
               stack.push(arr[i]); 
            }
            else if(container.containsKey(arr[i])){
                if(stack.isEmpty() || stack.pop() != container.get(arr[i])){
                    return false;
                }

            }
            
        }
        return stack.isEmpty();

        
    }
}