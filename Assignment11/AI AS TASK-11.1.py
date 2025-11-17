class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # Initialize the next pointer to null

class SinglyLinkedList:

    def __init__(self):
        """Initializes an empty list with a null head."""
        self.head = None
    def is_empty(self) -> bool:
        """Checks if the list is empty."""
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        # 1. New node's next pointer points to the current head
        new_node.next = self.head
        # 2. The list's head is updated to be the new node
        self.head = new_node
        print(f"Inserted '{data}' at the beginning.")

    def insert_at_end(self, data):
        new_node = Node(data)
        # Case 1: If the list is empty, the new node becomes the head
        if self.is_empty():
            self.head = new_node
            print(f"Inserted '{data}' at the end (new head).")
            return
        # Case 2: Traverse the list to find the last node
        current = self.head
        while current.next: # Loop until current.next is None (meaning current is the last node)
            current = current.next
        # 3. The last node's 'next' pointer is updated to the new node
        current.next = new_node
        print(f"Inserted '{data}' at the end.")
    def display(self):
        """
        Traverses the list from head to tail and prints all node data.
        """
        if self.is_empty():
            print("The list is empty.")
            return
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next # Move to the next node

        # Print the list elements clearly
        print("Linked List: " + " -> ".join(elements) + " -> None")
# --- Demonstration ---
if __name__ == '__main__':
    list = SinglyLinkedList()
    print("--- Initial State ---")
    list.display() # List is empty
    print("\n--- Insert at End ---")
    list.insert_at_end(10) # 10 -> None
    list.insert_at_end(20) # 10 -> 20 -> None
    list.display()
    print("\n--- Insert at Beginning ---")
    list.insert_at_beginning(5)  # 5 -> 10 -> 20 -> None
    list.insert_at_beginning(1)  # 1 -> 5 -> 10 -> 20 -> None
    list.display()
    print("\n--- Final Insertions ---")
    list.insert_at_end(30) # 1 -> 5 -> 10 -> 20 -> 30 -> None
    list.insert_at_beginning(0) # 0 -> 1 -> 5 -> 10 -> 20 -> 30 -> None
    list.display()
    # Illustrate the structure