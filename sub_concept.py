from concept import Concept

class SubConcept(Concept):
    def __init__(self, title, description, importance_level, related_topic):
        super().__init__(title, description, importance_level)
        self.related_topic = related_topic

    def display(self, depth=0):
        indent = " " * (depth * 4)
        print(f"{indent}{self.get_title()} (Bağlantılı: {self.related_topic})")
        print(f"{indent}   {self.get_description()}")
        for child in self.children:
            child.display(depth + 1)
