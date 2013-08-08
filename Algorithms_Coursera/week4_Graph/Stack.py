class Stack:
    def __init__(self,maxsize = 20):
        self.stack = []
        self.maxsize = maxsize
        self.top = -1

    def isFull(self):
        return True if len(self.stack) > self.maxsize + 1 else False
            
    def isEmpty(self):
        return True if self.top == -1 else False

    def pop(self):
        if self.isEmpty():
            raise "Stack is empty"
        else:
            retData = self.stack[-1]
            self.top -=1
            del self.stack[-1]
            return retData

    def push(self,pushData):
        if self.isFull():
            raise "Stack is full"
        else:
            self.stack.append(pushData)
            self.top += 1

            
            
        