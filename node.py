from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, title, description):
        self.__title = title
        self.__description = description
        self.children = []

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def add_child(self, node):
        self.children.append(node)

    def remove_child(self, title):
        self.children = [child for child in self.children if child.get_title() != title]

    @abstractmethod
    def display(self, depth=0):
        pass

