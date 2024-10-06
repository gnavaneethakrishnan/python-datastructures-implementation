class graph:

    def __init__(self) -> None:
        self.adjlist: dict = {}

    def add_vertex(self, vertex: str) -> bool:
        if vertex not in self.adjlist.keys():
            self.adjlist[vertex] = []
            return True
        return False

    def add_edges(self, vertex1: str, vertex2: str) -> bool:
        if (vertex1 and vertex2) in self.adjlist.keys():
            self.adjlist[vertex1].append(vertex2)
            self.adjlist[vertex2].append(vertex1)
            return True
        else:
            return False

    def print_graph(self) -> None:

        for key, value in self.adjlist.items():
            print(f"{key} : {value}")

    def remove_edge(self, vertex1: str, vertex2: str) -> bool:
        if (vertex1 and vertex2) in self.adjlist.keys():
            self.adjlist[vertex1].remove(vertex2)
            self.adjlist[vertex2].remove(vertex1)
            return True
        return False

    def remove_vertex(self, vertex1: str) -> bool:
        if vertex1 in self.adjlist.keys():
            for value in self.adjlist[vertex1]:
                self.adjlist[value].remove(vertex1)
            del self.adjlist[vertex1]
            return True
        return False


if __name__ == "__main__":
    my_graph = graph()
    my_graph.print_graph()
    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    my_graph.add_vertex("D")
    # my_graph.print_graph()
    my_graph.add_edges("A", "B")
    my_graph.add_edges("A", "C")
    my_graph.add_edges("A", "D")
    my_graph.add_edges("B", "D")
    my_graph.add_edges("C", "D")
    my_graph.print_graph()
    print("************")
    # my_graph.remove_edge("A", "D")
    my_graph.print_graph()
    my_graph.remove_vertex("A")
    print("******final******")
    my_graph.print_graph()
