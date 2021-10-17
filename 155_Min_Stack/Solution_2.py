class MinStack:
    def __init__(self):
        self.stack = list()
        self.mins = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        mins_temp = self.mins
        self.mins.append(val if not mins_temp else min(val, mins_temp[-1]))
            
    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()  

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]