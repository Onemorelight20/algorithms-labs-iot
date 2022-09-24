from vertex import Vertex


def get_file_content_list(filename: str):
    result = []
    with open(filename) as file:
        for line in file:
            result.append([int(ch) for ch in line.strip()])
    return result


def get_2d_list_element_neighbours(vertex: Vertex, data: list):
    max_row_idx = len(data) - 1
    max_column_idx = len(data[vertex.idx_row]) - 1
    neighbours = [
        data[max(0, vertex.idx_row - 1)][max(0, vertex.idx_column - 1)],
        data[max(0, vertex.idx_row - 1)][vertex.idx_column],
        data[max(0, vertex.idx_row - 1)][min(max_column_idx, vertex.idx_column + 1)],
        data[vertex.idx_row][min(max_column_idx, vertex.idx_column + 1)],
        data[min(max_row_idx, vertex.idx_row + 1)][min(max_column_idx, vertex.idx_column + 1)],
        data[min(max_row_idx, vertex.idx_row + 1)][vertex.idx_column],
        data[min(max_row_idx, vertex.idx_row + 1)][max(0, vertex.idx_column - 1)],
        data[vertex.idx_row][max(0, vertex.idx_column - 1)],
    ]
    return neighbours


def is_reachable(vertex: Vertex, data: list):
    if data[vertex.idx_row][vertex.idx_column] == 0:
        return False
    else:
        if get_2d_list_element_neighbours(vertex, data).count(0) > 0:
            return False
    return True


def get_available_neighbours(vertex: Vertex, data: list):
    max_row_idx = len(data) - 1
    max_column_idx = len(data[vertex.idx_row]) - 1
    available_neighbours = []
    neighbours_indexes = (
        (max(0, vertex.idx_row - 1), vertex.idx_column),
        (vertex.idx_row, min(max_column_idx, vertex.idx_column + 1)),
        (min(max_row_idx, vertex.idx_row + 1), vertex.idx_column),
        (vertex.idx_row, max(0, vertex.idx_column - 1))
    )
    for idx_row, idx_column in neighbours_indexes:
        cur_vertex = Vertex(idx_row, idx_column)
        if is_reachable(cur_vertex, data) and not cur_vertex == vertex and available_neighbours.count(cur_vertex) == 0:
            available_neighbours.append(cur_vertex)

    return available_neighbours


def get_adjecency_list(data: list):
    adjecency_list = {}
    for i, row in enumerate(data):
        for j, el in enumerate(row):
            vertex = Vertex(i, j)
            if is_reachable(vertex, data):
                adjecency_list[vertex] = get_available_neighbours(vertex, data)
    return adjecency_list


def write_result_to_file(filename: str, data: list, path: list):
    if path == -1:
        with open(filename, 'w') as file:
            file.write(str(-1))
            return

    path = set(path)
    with open(filename, 'w') as file:
        file.write(f'{str(len(path))}\n')
        for i, row in enumerate(data):
            for j, el in enumerate(row):
                if Vertex(i, j) in path:
                    file.write('+')
                else:
                    file.write(str(el))
            file.write('\n')


if __name__ == '__main__':
    data = get_file_content_list('input.txt')
    adj_l = get_adjecency_list(data)
    for vertex, neighbours in adj_l.items():
        print(vertex, ' -> ', neighbours)
