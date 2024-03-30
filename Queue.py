class Queue:
    def __init__(self):
        self.queue = []
        self.front =0
        self.rear =0

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return self.rear == len(self.queue) - 1

    def enqueue(self, item):
        if self.is_full():
            print("The queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue.append(item)

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue.pop(0)
        self.rear -=1

    def peek(self):
        if self.is_empty():
            print("The queue is empty")
        else:
            return self.queue[self.front]

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("The elements are:", queue.queue)
    queue.dequeue()
    print("The elements are:", queue.queue)
    queue.enqueue(10)
    print("The top most element of queue", queue.peek())
    print("The elements are:", queue.queue)
