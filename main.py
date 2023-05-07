from doublyLinkedList import DoublyLinkedList

dll = DoublyLinkedList()
dll.append(10)
print(dll.head.data)
dll.append(12)
print(dll.head.next.data)
print(dll.head.next.previous.data)