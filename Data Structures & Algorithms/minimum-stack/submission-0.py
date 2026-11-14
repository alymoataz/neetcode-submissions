class MinStack:

    def __init__(self):
        self.s=[]
        self.min_s=[]
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.min_s or val<=self.min_s[-1]:
            self.min_s.append(val)
        

    def pop(self) -> None:
        x=self.s.pop()
        if x==self.min_s[-1]:
            self.min_s.pop()

    def top(self) -> int:
        return self.s[-1]


    def getMin(self) -> int:
        return self.min_s[-1]
        
