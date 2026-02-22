class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, key=lambda x: x):
        self.root = None
        self.key = key

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if self.key(value) < self.key(current.value):
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
     
    def print_inorder(self):
      def _inorder(node):
        if node is None:
            return
        _inorder(node.left)
        print(node.value)
        _inorder(node.right)

        _inorder(self.root)

    def print_mermaid(self):
      print("graph TD")

    def _mermaid(node, name):
        if node is None:
            empty_name = name + "x"
            print(f"{empty_name}(( ))")
            print(f"style {empty_name} fill:#fff,stroke-width:0px")
            return

        print(f"{name}(({node.value}))")

        left_name = name + "l"
        print(f"{name} --> {left_name}")
        _mermaid(node.left, left_name)

        right_name = name + "r"
        print(f"{name} --> {right_name}")
        _mermaid(node.right, right_name)

        ד_mermaid(self.root, "t")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"{self.name} ({self.grade})"


if __name__ == "__main__":

   # תשובה לסעיף 4
   # t = Tree(key=lambda s: s.grade)
   # t.insert(Student("Dana", 87))
   # t.insert(Student("Avi", 92))
   # t.insert(Student("Noa", 75))
   # t.print_inorder()

   # תשובה לסעיף 5
   t = Tree()
   t.insert(10)
   t.insert(2)
   t.insert(4)
   t.insert(16)
   t.insert(15)
   t.insert(17)
   t.insert(20)

   t.print_mermaid()


