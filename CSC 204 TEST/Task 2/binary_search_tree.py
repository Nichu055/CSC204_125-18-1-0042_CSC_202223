from create_nodes import Node

class SingleLinkedList:
   def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#To convert the single linked list into a binary search tree

    def convert_to_bst(self, values):
        values.sort()
        
        def sorted_list_to_bst(start, end):
            if start > end:
                return None
            
            mid = (start + end) // 2
            root = Node(values[mid])
            root.left = sorted_list_to_bst(start, mid - 1)
            root.right = sorted_list_to_bst(mid + 1, end)
            return root
        
        return sorted_list_to_bst(0, len(values) - 1)

#To print the Binary Search Tree

bst_values = [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28]
bst_linked_list = SingleLinkedList()
for data in bst_values:
    bst_linked_list.insert(data)

bst_root = bst_linked_list.convert_to_bst(bst_values)
print("Binary Search Tree:")