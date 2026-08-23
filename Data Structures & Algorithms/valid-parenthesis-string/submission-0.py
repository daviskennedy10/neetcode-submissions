class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        for i in range(len(s)):
            if s[i] == "(":
                left_stack.append(i)
            if s[i] == "*":
                star_stack.append(i)
            if s[i] == ")":
                if not left_stack and not star_stack:
                    return False
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
        while left_stack:
            if not star_stack:
                return False
            if left_stack[-1] > star_stack[-1]:
                return False
            left_stack.pop()
            star_stack.pop()
        return True