class Stack:
    def __init__(self):
        self._items = []
        print("Stack initialized.")
    def is_empty(self) -> bool:     
        return len(self._items) == 0
    def push(self, item):
        self._items.append(item)
        print(f"Pushed: {item}. Current stack size: {len(self._items)}")
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        # pop() method on a list removes and returns the last element
        removed_item = self._items.pop()
        print(f"Popped: {removed_item}. Remaining size: {len(self._items)}")
        return removed_item
    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek into an empty stack.")
        # Get the last element without removing it
        return self._items[-1]
    def size(self) -> int:
        """Returns the number of items in the stack."""
        return len(self._items)
if __name__ == '__main__':
    my_stack = Stack()
    print("\nIs stack empty?", my_stack.is_empty())
    my_stack.push("A")
    my_stack.push("B")
    my_stack.push("C")
    top_item = my_stack.peek()
    print(f"\nPeeked at top item: {top_item}")
    print("Is stack empty after peek?", my_stack.is_empty())
    print("\nStarting Pop operations:")
    my_stack.pop()  # C
    my_stack.pop()  # B
    print(f"\nCurrent size: {my_stack.size()}")
    my_stack.pop() # A
    print("\nIs stack empty?", my_stack.is_empty())
    try:
        my_stack.pop()
    except IndexError as e:
        print(f"Caught expected error: {e}")