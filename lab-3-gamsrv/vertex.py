from enum import Enum


class VertexType(Enum):
    CLIENT = 1
    ROUTER = 2


class Vertex:
    def __init__(self, role: VertexType, index: int):
        self.role = role
        self.index = index

    def __str__(self):
        return f"({self.role}, {self.index})"

    def __repr__(self):
        return f"Vertex{self.__str__()}"

    def __eq__(self, other):
        if type(self) is type(other):
            return self.role is other.role and self.index is other.index
        else:
            return False

    def __hash__(self):
        return hash((self.role, self.index))
