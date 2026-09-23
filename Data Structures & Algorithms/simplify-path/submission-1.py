class Solution:
    def simplifyPath(self, path: str) -> str:
        # split elements in path by /
        raw = path.split('/')
        print(raw)
        # create stack
        stack = []
        # for loop over path:
        for i in range(len(raw)):
            element = raw[i]
            # if element is not . and not ..
            if element != '.' and element != '..' and element != '':
                # add it to the stack
                stack.append(element)
            # else if its .. and stack is not empty
            elif stack and element == '..':
                # pop from the stack
                stack.pop()
            # else if it . or it is "" and stack is not empty
            elif element == "" or element == ".":
                # continue
                continue
        
        # turn the stack to a string
        res = "/" + "/".join(stack)
        # return the string
        return res
