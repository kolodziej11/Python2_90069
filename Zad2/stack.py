class Stack:
    def __init__(self):
        self.__m_buffer = []

    def push(self, element):
        self.__m_buffer.append(element)

    def top(self):
        return self.__m_buffer[-1]

    def pop(self):
        self.__m_buffer.pop()

    def size(self):
        return len(self.__m_buffer)

    def is_empty(self):
        return self.size() == 0


class BroadStack(Stack):
    def __init__(self):
        super().__init__()
        self.min = None

    def push(self, element):
        super().push(element)
        self.minimum()

    def minimum(self):
        if self.min is None:
            self.min = self.top()
        else:
            if self.top() < self.min:
                self.min = self.top()

    def get_minimum(self):
        return self.min
