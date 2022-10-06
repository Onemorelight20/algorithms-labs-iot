class Edge:
    def __init__(self, from_vertex: int, to_vertex: int, retention: int):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.retention = retention

    def __str__(self):
        return f"({self.from_vertex}, {self.to_vertex}, {self.retention})"

    def __repr__(self):
        return f"Edge{self.__str__()}"

    def __eq__(self, other):
        if type(self) is type(other):
            return (self.from_vertex is other.from_vertex
                    and self.to_vertex is other.to_vertex
                    and self.retention is other.retention)
        else:
            return False
