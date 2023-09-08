class Stack:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list.pop()
 