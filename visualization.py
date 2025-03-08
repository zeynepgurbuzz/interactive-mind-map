import matplotlib.pyplot as plt
import networkx as nx
from mind_map import MindMap

class Visualization:
    def __init__(self, mind_map):
        self.mind_map = mind_map

    def show_graph(self):
        G = nx.DiGraph()

        for concept in self.mind_map.concepts:
            G.add_node(concept.get_title())

        for concept in self.mind_map.concepts:
            if hasattr(concept, "children"):
                for child in concept.children:
                    G.add_edge(concept.get_title(), child.get_title())

        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color="skyblue", edge_color="gray", node_size=3000, font_size=10)
        plt.title("🧠 Zihin Haritası Görselleştirme")
        plt.show()

if __name__ == "__main__":
    my_mind_map = MindMap("Zihin Haritam")
    visualizer = Visualization(my_mind_map)
    visualizer.show_graph()
