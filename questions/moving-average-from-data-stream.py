from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size_ = size
        self.window = 0
        self.current = 0
        self.re = None
        self.queue = deque([])


    def next(self, val: int) -> float:

        if (self.window < self.size_):
            if not self.re:
                self.re = val
            self.current = (self.current + val)
            self.window += 1
            self.queue.append(val)
            #print(self.queue)
            return self.current / self.window
        else:
            p = self.queue.popleft()
            self.current = self.current + val - p
            #print("haiiii")
            #print(self.queue)
            self.queue.append(val)
            return self.current / self.size_


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
