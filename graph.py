class graph:

    def __init__(self) -> None:
        self.adjlist: dict = {}

    def add_vertex(self, vertex: str) -> bool:
        if vertex not in self.adjlist.keys():
            self.adjlist[vertex] = []
            return True
        return False

    def add_edges(self, vertex: str, edge: str) -> bool:
        if vertex in self.adjlist.keys():
            self.adjlist[vertex].append(edge)
            return True
        else:
            return False

    def print_graph(self) -> None:

        for key, value in self.adjlist.items():
            print(f"{key} : {value}")


if __name__ == "__main__":
    my_graph = graph()
    my_graph.print_graph()
    my_graph.add_vertex("A")
    my_graph.print_graph()
    my_graph.add_edges("A", "B")
    my_graph.print_graph()
