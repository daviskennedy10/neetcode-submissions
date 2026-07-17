class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in range(len(tokens)):
            if tokens[i] in "+*-/":
                number_a = stack.pop()
                number_b = stack.pop()
                if tokens[i] == "+":
                    num_a = int(number_a)
                    num_b = int(number_b)
                    stack.append(num_a+num_b)
                elif tokens[i] == "-":
                    num_a = int(number_a)
                    num_b = int(number_b)
                    stack.append(num_b-num_a)
                elif tokens[i] == "*":
                    num_a = int(number_a)
                    num_b = int(number_b)
                    stack.append(num_a*num_b)
                elif tokens[i] == "/":
                    num_a = int(number_a)
                    num_b = int(number_b)
                    stack.append(int(num_b/num_a))
            else:
                stack.append(tokens[i])

        return int(stack[-1])
