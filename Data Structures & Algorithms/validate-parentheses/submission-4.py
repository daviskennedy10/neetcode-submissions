class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == "{" or s[i] == "[" or s[i] == "(":
                stack.append(s[i])
            elif s[i] == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            elif s[i] == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif s[i] == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
        if stack:
            return False
        return True