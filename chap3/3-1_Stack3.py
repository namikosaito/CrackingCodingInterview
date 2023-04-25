# coding: utf-8
"""
一つの配列を使って、三つのスタックを実装する
"""

class MultiStack:
    def __init__(self, stack_size, number_of_stacks):
        self.number_of_stacks = number_of_stacks
        self.stack_sizes = stack_size
        self.array = [0] * (stack_size * number_of_stacks)
        self.sizes = [0] * number_of_stacks
        

    def push(self, value, stack_num):
        self._check_stack_num(stack_num)
        if self.is_full(stack_num):
            raise StackFullError("Push failed: stack is full")
        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = value
        
    def pop(self, stack_num):
        self._check_stack_num(stack_num)
        if self.is_empty(stack_num):
            raise StackEmptyError("Cannot pop from empty stack #{stack_num}")
        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return value
    
    def peek(self, stack_num):
        self._check_stack_num(stack_num)
        if self.is_empty(stack_num):
            raise StackEmptyError("Cannot peek at empty stack #{stack_num}")
        return self.array[self.index_of_top(stack_num)]
        
    def is_empty(self, stack_num):
        self._check_stack_num(stack_num)
        return self.sizes[stack_num] == 0

    def index_of_top(self,stack_num):
        self._check_stack_num(stack_num)
        return self.sizes[stack_num] == self.stack_sizes

    def is_full(self, stack_num):
        self._check_stack_num(stack_num)
        return self.sizes[stack_num] == self.stack_sizes
    
    def _check_stack_num(self, stack_num):
        if stack_num >= self.number_of_stacks:
            raise StackDoesNotExistError("Stack #{stack_num} does not exist")


class MultiStackError(Exception):
    """multistack operation error"""


class StackFullError(MultiStackError):
    """the stack is full"""


class StackEmptyError(MultiStackError):
    """the stack is empty"""


class StackDoesNotExistError(ValueError):
    """stack does not exist"""

if __name__ == "__main__":
    newstack = MultiStack(2, 2)
    print(newstack.is_empty(1))
    newstack.push(3, 1)
    print(newstack.peek(1))
    print(newstack.is_empty(1))
    newstack.push(2, 1)
    print(newstack.peek(1))
    print(newstack.pop(1))
    print(newstack.peek(1))
    newstack.push(3, 1)