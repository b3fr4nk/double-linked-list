from node import Node

class DoublyLinkedList:
  
  def __init__(self):
    self.head = None
    self.tail = None

  # TODO: append()
  #Add to the end of the linked list
  def append(self, new_data):
    if self.head is None:#empty linked list
      new_node = Node(new_data)
      self.head = new_node
      self.tail = new_node
    else:
      #create a new node
      new_node = Node(new_data)
      #set new node previous to tail
      new_node.previous = self.tail
      #set old tail.next to new node
      old_tail = self.tail
      old_tail.next = new_node
      #set tail to new node
      self.tail = new_node

  # TODO: insert()
  def insert(self, item, index):
    curr_index = 0
    curr_node = self.head

    while curr_index < index:
      curr_node = curr_node.next
      curr_index += 1

    new_node = Node(item)

    prev_node = curr_node.previous
    new_node.next = prev_node.next
    prev_node.next = new_node

    curr_node.previous = new_node
    

  # TODO: remove()
  def remove(self, value):
    node = self.head
    while node.data != value:
      node = node.next

    prev_node = node.previous
    next_node = node.next

    prev_node.next = next_node
    next_node.previous = prev_node

  # TODO: update()
  #Find and existing node with data == item and update with new value
  #traverse to find node
  #replace the data with value
  #hint: look at find() for singly linked list
  def update(self, item, value):
    node = self.head
    while node.data != item:
      node = node.next
      if node is None:
        raise KeyError('item is not in linked list')
    
    

    node.data = item

  # TODO: find()
  def find(self, item):
    node = self.head
    while node.data != item:
      node = node.next
      if node is None:
        raise KeyError('item is not in linked list')

    
    
    return node

  def __repr__(self):
    items = []
    curr_node = self.head
    while curr_node.next is not None:
      items.append(curr_node.data)
      curr_node = curr_node.next
    
    items.append(self.tail.data)

    return f'{items}'

# tesing
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)

node0.next = node1
node1.previous = node0
node1.next = node2
node2.previous = node1

llist = DoublyLinkedList()

llist.head = node0
llist.tail = node2

llist.insert(3, 1)
llist.remove(1)
llist.update(3, 4)
print(llist.find(0).data)

print(llist)