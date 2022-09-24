from queue import Queue
from vertex import Vertex


class Graph:
    def __init__(self, adjecency_list):
        self.adjecency_list = adjecency_list

    def bfs(self, start: Vertex, end: Vertex):
        visited = {}
        level = {}
        parent_of_vertex = {}
        bfs_traversal_output = []
        queue = Queue()

        for node in self.adjecency_list.keys():
            visited[node] = False
            parent_of_vertex[node] = None
            level[node] = -1

        required_vertex = end

        visited[start] = True
        level[start] = 0
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

        # shortest path from source node to any node
        if required_vertex not in parent_of_vertex:
            return -1

        path = []
        while required_vertex is not None:
            path.append(required_vertex)
            required_vertex = parent_of_vertex[required_vertex]
        path.reverse()
        return path
