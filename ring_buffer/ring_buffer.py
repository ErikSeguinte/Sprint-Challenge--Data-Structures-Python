from collections import deque

class RingBuffer:
    def __init__(self, capacity):
        self.storage = deque()
        self.capacity = capacity
        self._position = 0

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position % self.capacity

    def append(self, new_item):
        if len(self.storage) < self.capacity:
            self.storage.append(new_item)
        else:
            self.storage[self.position] = new_item

        self.position += 1


    def get(self):
        return list(self.storage)