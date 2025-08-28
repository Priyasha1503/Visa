
#https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack=[]
        self.minval=float('inf')
    def push(self, val: int) -> None:
        if self.stack!=[]:
            self.minval=min(self.minval,val)
            self.stack.append((val,self.minval))
        else:
            self.stack.append((val,val))

    def pop(self) -> None:
        if self.stack!=[]:
            self.stack.pop()
            if self.minval==self.stack[-1]:
                

    def top(self) -> int:
        if self.stack!=[]:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if self.stack!=[]:
            return self.stack[-1][1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
