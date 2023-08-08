class QueueUsingLinkedList:
    def __init__(self):
        self.queue = SingleLinkedList()

    def enqueue(self, data):
        self.queue.insert(data)

    def dequeue(self):
        if self.queue.head:
            data = self.queue.head.data
            self.queue.head = self.queue.head.next
            return data
        else:
            return None

    def display(self):
        self.queue.display()

# Run QueueUsingLinkedList
queue = QueueUsingLinkedList()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print("Queue:")
queue.display()

print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())

print("Queue after dequeuing:")
queue.display()
