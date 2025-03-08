from node import Node

class Concept(Node):
    def __init__(self, title, description, importance_level):
        super().__init__(title, description)
        self.importance_level = importance_level

    def display(self, depth=0):
        indent = " " * (depth * 4)
        print(f"{indent}{self.get_title()} (Önem: {self.importance_level})")
        print(f"{indent}   {self.get_description()}")
        for child in self.children:
            child.display(depth + 1)
