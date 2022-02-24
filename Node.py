# Модуль, содержащий реализацию системы непересекающихся множеств


class Node:
    def __init__(self):
        self.root = self

    def find(self):
        if self.root == self:
            return self
        else:
            self.root = self.root.find()
            return self.root

    def union(self, node):
        root1 = self.find()
        root2 = node.find()
        root1.root = root2

    def is_connect(self, node):
        return self.root.find() == node.root.find()
