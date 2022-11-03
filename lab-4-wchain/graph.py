from queue import Queue


class Graph:
    def __init__(self, adjecency_list: dict[str:list[str]]):
        self.adjecency_list = adjecency_list

    # bfs is modified to find the longest path from given node
    def bfs(self, start: str) -> list[str]:
        visited = {}
        level = {}
        parent_of_vertex = {}
        bfs_traversal_output = []
        queue = Queue()

        for node in self.adjecency_list.keys():
            visited[node] = False
            parent_of_vertex[node] = None
            level[node] = -1

        visited[start] = True
        level[start] = 1
        queue.put(start)
        while not queue.empty():
            vertex = queue.get()
            bfs_traversal_output.append(vertex)
            for vertex_neighbour in self.adjecency_list[vertex]:
                if not visited[vertex_neighbour]:
                    visited[vertex_neighbour] = True
                    parent_of_vertex[vertex_neighbour] = vertex
                    level[vertex_neighbour] = level[vertex] + 1
                    queue.put(vertex_neighbour)

        required_vertex = max(level, key=level.get)
        longest_path = []
        while required_vertex is not None:
            longest_path.append(required_vertex)
            required_vertex = parent_of_vertex[required_vertex]
        longest_path.reverse()

        return longest_path
