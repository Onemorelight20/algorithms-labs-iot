class Vertex:
    def __init__(self, idx_row, idx_column):
        self.idx_row = idx_row
        self.idx_column = idx_column

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'({self.idx_row},{self.idx_column})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __hash__(self):
        return hash((self.idx_row, self.idx_column))
