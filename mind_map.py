class MindMap:
    def __init__(self, title):
        self.title = title
        self.concepts = []

    def add_concept(self, concept):
        self.concepts.append(concept)

    def remove_concept(self, title):
        self.concepts = [concept for concept in self.concepts if concept.get_title() != title]

    def display_map(self):
        print(f"\n{self.title} - Zihin Haritası")
        for concept in self.concepts:
            concept.display()
