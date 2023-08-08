#using Bubblesort to sort the queue

def sort_queue(queue):
    items = []
    while True:
        item = queue.dequeue()
        if item is None:
            break
        items.append(item)

    # Bubble sort the items
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    sorted_queue = QueueUsingLinkedList()
    for item in items:
        sorted_queue.enqueue(item)

    return sorted_queue

# Run the sorted queue
queue.enqueue(12)
queue.enqueue(5)
queue.enqueue(8)
queue.enqueue(3)

print("Original Queue:")
queue.display()

sorted_queue = sort_queue(queue)
print("Sorted Queue:")
sorted_queue.display()
