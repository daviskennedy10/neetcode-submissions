class MinStack:


    def __init__(self):
        self.stack = []
        self.q = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.q or val <= self.q[0]:
            self.q.appendleft(val)
        else:
            self.q.append(val)
        

    def pop(self) -> None:
        number = self.stack[-1]
        if self.q[0] == number:
            self.q.popleft()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.q[0]
