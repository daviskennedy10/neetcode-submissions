class Solution:
    def decodeString(self, s: str) -> str:
        # create stack
        stack = []

        # for loop in s:
        for i in range(len(s)):
            # element = s[i]
            element = s[i]
            # create prev as empty string
            prev = ""
            # if element is ] and stack:
            if element == ']' and stack:
                # while stack and stack[-1] is not [:
                while stack and stack[-1] != '[':
                    # prev += stack.pop()
                    popped = stack.pop()
                    prev = popped + prev
                # if stack exists and stack[-1] is [:
                if stack and stack[-1] == '[':
                    # pop from the stack
                    stack.pop()
                # curr_number = 0 
                curr_num = ""

                # while stack and stack[-1] is a number:
                while stack and stack[-1].isdigit():
                    # curr_number = 10 * curr_number + int(stack[-1])
                    curr_num += stack[-1]
                    stack.pop()
                # encoded = prev.reverse() * curr_number
                encoded = prev * int(curr_num[::-1])
                # push encoded in to the stack
                stack.append(encoded)
                

            # if element is a letter or [:
            else:
                # put it in stack
                stack.append(element)
        # return stack converted to string
        res = "".join(stack)
        return res