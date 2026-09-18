class MyStack:

    def __init__(self):
        self.qa = deque()
        self.qb = deque()

    def push(self, x: int) -> None:
        self.qa.append(x)
        self.qb.append(x)
        

    def pop(self) -> int:
        return self.qa.pop()

    def top(self) -> int:
        return self.qa[-1]
        

    def empty(self) -> bool:
        if self.qa :
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()