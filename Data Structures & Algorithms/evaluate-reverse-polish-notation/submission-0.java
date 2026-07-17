class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        ArrayList<String> list = new ArrayList<>();
        list.add("*");
        list.add("/");
        list.add("-");
        list.add("+");
        for(int i = 0; i < tokens.length; i++){
            if(!list.contains(tokens[i])){
                int placer = Integer.parseInt(tokens[i]);
                stack.push(placer);
            }
            else{
                    int a = stack.pop();
                    int b = stack.pop();
                    int c ;
                    if(tokens[i].equals("+")){
                        c = a + b;
                    }
                    else if(tokens[i].equals("-")){
                        c = b - a;
                    }
                    else if(tokens[i].equals("/")){
                        c = b / a;
                    }
                    else{
                        c = b * a;
                    }
                    stack.push(c);
                }
            }
        return stack.peek();
        }
        
    }