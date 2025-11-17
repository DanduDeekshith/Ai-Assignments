class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        """Initializes an empty BST with a null root."""
        self.root = None
        print("Binary Search Tree initialized.")

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
        print(f"Inserted: {key}")

    def _insert_recursive(self, root_node: Node, key: int) -> Node:
        # Base case: If the current subtree is empty, return a new node
        if root_node is None:
            return Node(key)
        # Recursive step: Traverse left or right
        if key < root_node.key:
            root_node.left = self._insert_recursive(root_node.left, key)
        elif key > root_node.key:
            root_node.right = self._insert_recursive(root_node.right, key)
        # If key is equal (duplicates are ignored in this simple implementation), do nothing.
        return root_node
    def inorder_traversal(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        print("\nIn-order Traversal (Sorted):", " -> ".join(map(str, elements)))
    def _inorder_recursive(self, root_node: Node, elements: list):
        if root_node:
            # 1. Recurse on the left child
            self._inorder_recursive(root_node.left, elements)
            # 2. Visit the current node (add its key to the list)
            elements.append(root_node.key)
            # 3. Recurse on the right child
            self._inorder_recursive(root_node.right, elements)
# --- Demonstration of BST Usage ---
if __name__ == '__main__':
    bst = BinarySearchTree()
    # Insert keys in a non-sorted order (e.g., to create an unbalanced tree)
    keys = [50, 30, 70, 20, 40, 60, 80]
    print("--- Inserting Keys ---")
    for key in keys:
        bst.insert(key)
    print("\n--- Performing Traversal ---")
    # This will print the keys in sorted order: 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80
    bst.inorder_traversal()