class MinStack:

    def __init__(self):
        self.minstack = []
        self.mainstack = []

    def push(self, val: int) -> None:
        self.mainstack.append(val)
        if len(self.minstack) > 0 and self.minstack[len(self.minstack)-1] < val:
            self.minstack.append(self.minstack[len(self.minstack)-1])
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.mainstack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.mainstack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
