class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        # Add data to left subtree
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
        
    def in_order_traversal(self):
        elements = []

        # Visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        
        # Visit base node
        elements.append(self.data)

        # Visit right tree
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range (1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    nameLetters = ["R", "O", "N", "N", "I", "E", "D", "A", "Z", "A"]
    letter_tree = build_tree(nameLetters)

    print("R is in the list?", letter_tree.search("R"))
    print("O is in the list?", letter_tree.search("O"))
    print("N is in the list?", letter_tree.search("N"))
 
    print("J is in the list?", letter_tree.search("J"))
    print("L is in the list?", letter_tree.search("L"))
    print("P is in the list?", letter_tree.search("P"))

    print(letter_tree.in_order_traversal())
