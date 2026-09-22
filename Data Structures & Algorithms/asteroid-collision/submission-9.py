class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        ast_sign =""
        
        for ast in asteroids:
            ast_sign = "left" if ast < 0 else "right"

            while stack and (ast_sign == "left" and stack[-1] > 0):
                if abs(stack[-1]) == abs(ast):
                    stack.pop()
                    break
                elif abs(ast) > abs(stack[-1]):
                    stack.pop()
                else:
                    break
            else:
                stack.append(ast)
        return stack
        