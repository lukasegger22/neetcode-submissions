class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []
    def push(self, val: int) -> None:
        if len(self.minstack) < 1 or val <= self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])
        self.stack.append(val)
    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minstack[-1]
