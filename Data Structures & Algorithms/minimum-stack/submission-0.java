class MinStack {
   private ArrayList<Integer> stack;
   private ArrayList<Integer> checker;
    public MinStack() {
      stack = new ArrayList<>();
      checker = new ArrayList<>();   
    }
    
    public void push(int val) {
        stack.add(val);
        if(checker.size() == 0){
            checker.add(val);
        }
        else if(val < checker.get(checker.size()-1)){
            checker.add(val);
        }
        else{
            checker.add(checker.get(checker.size()-1));
        }
    }
    
    public void pop() {
        stack.remove(stack.size()-1);
        checker.remove(checker.size()-1);
        
    }
    
    public int top() {
        return stack.get(stack.size()-1);
    }
    
    public int getMin() {
        return checker.get(checker.size()-1);
    }
}
