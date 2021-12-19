# We can have a custom class to mimic the functionality of a queue
from collections import deque
import threading
import time


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

    def place_order(self, orders):
        for order in orders:
            print('Placing order for '+str(order))
            self.enqueue(order)
            time.sleep(0.5)

    def serve_order(self):
        time.sleep(1)
        while self.size() != 0:
            current_order = self.dequeue()
            print('serving '+current_order+' now.')
            time.sleep(2)

    def produce_binary_numbers(self, n):
        q = Queue()
        q.enqueue('1')
        for i in range(n):
            front = q.front()
            print("   ", front)
            q.enqueue(front + "0")
            q.enqueue(front + "1")
            q.dequeue()


if __name__ == '__main__':
    q = Queue()
    # q.enqueue({
    #     'company': 'Walmart',
    #     'timestamp': '7th Dec, 11:00 PM',
    #     'price': 131.10
    # })
    # q.enqueue({
    #     'company': 'Walmart',
    #     'timestamp': '7th Dec, 11:01 PM',
    #     'price': 132
    # })
    # q.enqueue({
    #     'company': 'Walmart',
    #     'timestamp': '7th Dec, 11:02 PM',
    #     'price': 135
    # })
    # print(q.buffer)
    # print(q.size())
    # print(q.is_empty())

    # orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    # t1 = threading.Thread(target=q.place_order, args=(orders,))
    # t2 = threading.Thread(target=q.serve_order)
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    q.produce_binary_numbers(10)


'''
Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.
'''


'''
Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

You also need to add front() function in queue class that can return the front element in the queue.
'''
