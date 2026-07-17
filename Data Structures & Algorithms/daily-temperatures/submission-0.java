class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        Stack<Integer> stackB = new Stack<>();
        int[] res = new int[temperatures.length];
        for(int i = temperatures.length-1; i >= 0; i--){
            stack.push(temperatures[i]);
        }
        for(int j = 0; j < temperatures.length; j++){
            int count = 0;
            int waste = stack.pop();
            while(!stack.isEmpty()){
                int value = stack.pop();
                if(value <= temperatures[j]){
                    count++;
                }
                stackB.push(value);
                if(value > temperatures[j]){
                    count++;
                    break;
                }
                if(stack.isEmpty()){
                    count = 0;
                }
            }
            while(!stackB.isEmpty()){
                stack.push(stackB.pop());
            }
            res[j] = count;
        }
        return res;
    }
}
