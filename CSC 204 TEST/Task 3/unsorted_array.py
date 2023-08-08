from create_nodes import Node

#An algorithm to implement a binar search algorithm on an unsorted array.

def binary_search_unsorted(arr, target):
    # Create a linked list out of the unsorted array for searching 
    linked_list = SingleLinkedList()
    for data in arr:
        linked_list.insert(data)

    current = linked_list.head
    while current:
        if current.data == target:
            return True
        current = current.next
 Queue data
    return False

# Run binary_search_unsorted
arr = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
target = 15
print(f"Target {target} found: {binary_search_unsorted(arr, target)}")
