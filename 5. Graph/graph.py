import display

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [LinkedList() for _ in range(vertices)]

    def add_edge(self, src, dest):
        self.graph[src].add(dest)
        self.graph[dest].add(src)  # For an undirected graph

    def get_edges(self):
        edges = []
        for i in range(self.vertices):
            for dest in self.graph[i]:
                edges.append((i, dest))
        return edges



if __name__ == "__main__":
    g = Graph(5)  # Create a graph with 5 vertices
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    display.display_graphical(g)
