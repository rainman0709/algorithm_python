from Queue import *

my_queue = Queue(4)

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

my_queue.showQueue()

my_queue.dequeue()

my_queue.showQueue()