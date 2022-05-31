# Written by Yuta

class EmptyQueueError(Exception):
    def __init__(self, message):
        self.message = message

class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def peek_at_front(self):
        if self.is_empty():
            raise EmptyQueueError('Cannot peek at front of empty queue')
        return self._data[0]

    def peek_at_back(self):
        if self.is_empty():
            EmptyQueueError('Cannot peek at back of empty queue')
        return self._data[-1]

    # if dont use insert, may need other class members
    def enqueue(self, data):
        self._data.insert(0, data)

    def dequeue(self):
        return self._data.pop()
