# Written by Yuta

class EmptyStackError(Exception):
    def __init__(self, message):
        self.message = message

class Stack:
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def peek(self):
        if self.is_empty():
            raise EmptyStackError('Cannot peek at top of empty stack')
        return self._data[-1]

    def push(self, data):
        self._data.append(data)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('Cannot pop from top of empty stack')
        return self._data.pop()