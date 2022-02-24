from Node import Node


# Ячейка, set_num отвечает за множество, в котором ячейка находится, is_visited - метка посещений
class Cell:
    def __init__(self):
        self.left = None
        self.right = None
        self.top = None
        self.bot = None
        self.set_num = Node()
        self.is_visited = 0
