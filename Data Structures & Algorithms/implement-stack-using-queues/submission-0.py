class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.stack.reverse()
        print(self.stack)
        res = self.stack.pop(0)
        self.stack.reverse()
        print(self.stack)

        return res

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if self.stack:
            return False
        
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()