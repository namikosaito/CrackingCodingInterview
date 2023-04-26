# coding: utf-8
"""
pop, pushに加えて、最小の要素を返す関数minを持つスタックをデザインする
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if self.items:
            return self.items[-1]
        return None
    
class Minstack(Stack):
    def __init__(self):
        super().__init__()
        self.minvals = Stack()
        
    def push(self, value):
        super().push(value)
        if self.minimum() == None:
            self.minvals.push(value)
            
        elif not self.minvals or value <= self.minimum():
            self.minvals.push(value)
            
    def pop(self):
        value = super().pop()
        if value == self.minimum():
            self.minvals.pop()
        return value
    
    def minimum(self):
        return self.minvals.peek()
    
    
if __name__ == "__main__":
    test_stack = Minstack()
    assert test_stack.minimum() is None
    print(test_stack.minimum())
    
    test_stack.push(5)
    assert test_stack.minimum() == 5
    print(test_stack.minimum())
    
    test_stack.push(6)
    assert test_stack.minimum() == 5
    print(test_stack.minimum())
    
    test_stack.push(3)
    assert test_stack.minimum() == 3
    print(test_stack.minimum())
    
    test_stack.push(7)
    assert test_stack.minimum() == 3
    print(test_stack.minimum())

    test_stack.push(3)
    assert test_stack.minimum() == 3
    print(test_stack.minimum())

    test_stack.pop()
    assert test_stack.minimum() == 3
    print(test_stack.minimum())

    test_stack.pop()
    assert test_stack.minimum() == 3
    print(test_stack.minimum())

    test_stack.pop()
    assert test_stack.minimum() == 5
    print(test_stack.minimum())

    test_stack.push(1)
    assert test_stack.minimum() == 1
    print(test_stack.minimum())
    
    