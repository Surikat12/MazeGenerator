from Node import Node

class NodeTests:
    def test_union_two_node(self):
        node_1 = Node()
        node_2 = Node()
        node_1.union(node_2)
        if node_1.root == node_2:
            return "Test union_two_node: Pass"
        return "Test union_two_node: Failed"

    def test_union_node_and_graph(self):
        node_1 = Node()
        node_2 = Node()
        node_3 = Node()
        node_1.union(node_2)
        node_2.union(node_3)
        if node_1.find() == node_3:
            return "Test union_node_and_graph: Pass"
        return "Test union_node_and_graph: Failed"

    def test_find_itself(self):
        node_1 = Node()
        if node_1.find() == node_1:
            return "Test find_itself: Pass"
        return "Test find_itself: Failed"

    def test_find_root_in_node_2(self):
        node_1 = Node()
        node_2 = Node()
        node_1.union(node_2)
        if node_1.find() == node_2:
            return "Test find_root_in_node_2: Pass"
        return "Test find_root_in_node_2: Failed"

    def test_is_not_connected(self):
        node_1 = Node()
        node_2 = Node()
        if not node_1.is_connect(node_2):
            return "Test is_not_connected: Pass"
        return "Test is_not_connected: Failed"

    def test_is_connected(self):
        node_1 = Node()
        node_2 = Node()
        node_1.union(node_2)
        if node_1.is_connect(node_2):
            return "Test is_connected: Pass"
        return "Test is_connected: Failed"
        

nodeTests = NodeTests()
print(nodeTests.test_union_two_node())
print(nodeTests.test_union_node_and_graph())
print(nodeTests.test_find_itself())
print(nodeTests.test_find_root_in_node_2())
print(nodeTests.test_is_not_connected())
print(nodeTests.test_is_connected())

