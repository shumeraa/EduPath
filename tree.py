class classNode:
    def __init__(self):
        self.children = [None] * 26  # A node can have up to 26 children (one for each letter)
        self.is_end = False  # Flag to indicate the end of a class code
        self.vector = None  # To store the vector at the end of a class code

    def set_vector(self, vector):
        self.vector = vector
        self.is_end = True

    def get_child_index(self, char):
        return ord(char.upper()) - ord('A')  # Convert character to index (0-25)

    def has_child(self, char):
        return self.children[self.get_child_index(char)] is not None

    def get_child(self, char):
        return self.children[self.get_child_index(char)]

    def add_child(self, char):
        self.children[self.get_child_index(char)] = classNode()


class classTree:
    def __init__(self):
        self.root = classNode()

    def insert(self, class_code, vector):
        node = self.root
        for char in class_code:
            if not node.has_child(char):
                node.add_child(char)
            node = node.get_child(char)
        node.set_vector(vector)  # Set the vector at the final node

    def get_vector(self, class_code):
        node = self.root
        for char in class_code:
            if not node.has_child(char):
                return None  # Class code not found
            node = node.get_child(char)
        return node.vector if node.is_end else None  # Return the vector if this is the end of a class code