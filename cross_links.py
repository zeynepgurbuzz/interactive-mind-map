import json

class CrossLinks:
    def __init__(self, filename="links.json"):
        self.filename = filename
        self.links = self.load_links()

    def load_links(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_links(self):
        with open(self.filename, "w") as file:
            json.dump(self.links, file, indent=4)

    def add_link(self, concept1, concept2):
        if concept1 not in self.links:
            self.links[concept1] = []
        if concept2 not in self.links[concept1]:
            self.links[concept1].append(concept2)
        if concept2 not in self.links:
            self.links[concept2] = []
        if concept1 not in self.links[concept2]:
            self.links[concept2].append(concept1)
        self.save_links()
        print(f"🔗 {concept1} ↔ {concept2} bağlantısı eklendi!")

    def show_links(self):
        if not self.links:
            print("📌 Henüz hiç bağlantı eklenmedi.")
            return
        print("\n📌 Kavram Bağlantıları:")
        for concept, related in self.links.items():
            print(f"{concept} ↔ {', '.join(related)}")
