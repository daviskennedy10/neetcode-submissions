class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = 0
        n = len(operations)
        
        stack = []
        for i in range(n):
            symbol = operations[i]
            if ((symbol != '+' and symbol != 'C') and symbol != 'D'):
                number = int(symbol)
                stack.append(number)
            elif symbol == '+' and len(stack) >= 2:
                first = stack.pop()
                put = first + stack[-1]
                stack.append(first)
                stack.append(put)
            elif symbol == 'C':
                stack.pop()
            elif symbol == 'D':
                stack.append(stack[-1] + stack[-1])


        print(stack)
        return sum(stack)
                

