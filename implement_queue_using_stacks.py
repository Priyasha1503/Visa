#https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.input_stack=[]
        self.output_stack=[]

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        if self.output_stack!=[]:
            return self.output_stack.pop()
        else:
            #all input to output
            while self.input_stack:
                d=self.input_stack.pop()
                self.output_stack.append(d)
            if self.output_stack:
                return self.output_stack.pop()
    def peek(self) -> int:
        if self.output_stack!=[]:
            return self.output_stack[-1]
        else:
            # all input to output
            while self.input_stack:
                d=self.input_stack.pop()
                self.output_stack.append(d)
            if self.output_stack:
                return self.output_stack[-1]

    def empty(self) -> bool:
        if self.input_stack==[] and self.output_stack==[]:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
