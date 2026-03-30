class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        

    def pop(self) -> None:
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        min_ = self.arr[0]
        for i in self.arr:
            min_ = min(i,min_)
        return min_
        
