class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None

  def append(self, data):
   
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def prepend(self, data):
   
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def delete(self, key):
   
    current_node = self.head
    if current_node and current_node.data == key:
      self.head = current_node.next
      current_node = None
      return
    prev_node = None
    while current_node and current_node.data != key:
      prev_node = current_node
      current_node = current_node.next
    if current_node is None:
      return
    prev_node.next = current_node.next
    current_node = None

  def search(self, key):
    
    current_node = self.head
    while current_node:
      if current_node.data == key:
        return True
      current_node = current_node.next
    return False

  def insert_after_node(self, prev_node, data):
   
    if not prev_node:
      print("Previous node is not in the linked list.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def print_list(self):
    """Print the elements of the linked list."""
    current_node = self.head
    while current_node:
      print(current_node.data, end=" -> ")
      current_node = current_node.next
    print("None")


# Example usage:
if __name__ == "__main__":
  linked_list = LinkedList()
  linked_list.append(1)
  linked_list.append(2)
  linked_list.append(4)

  linked_list.prepend(0)

  linked_list.print_list()

  key_to_search = 2
  if linked_list.search(key_to_search):
    print(f"{key_to_search} is found in the linked list.")
  else:
    print(f"{key_to_search} is not found in the linked list.")

  prev_node = linked_list.head.next  # Node with data 1
  linked_list.insert_after_node(prev_node, 3)

  linked_list.print_list()
