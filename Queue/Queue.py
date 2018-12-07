class Queue(object):
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self,data):
        if self.isfull():
            raise Exception('the queue is full!')
        else:
            self.queue.append(data)
            self.rear += 1

    def dequeue(self):
        if self.isempty():
            raise Exception('the queue is empty!')
        else:
            self.queue.pop(0)
            self.rear -= 1

    def isfull(self):
        if self.size == self.rear - self.front + 1:
            return True
        else:
            return False

    def isempty(self):
        if self.rear == -1:
            return True
        else:
            False

    def showQueue(self):
        print(self.queue)