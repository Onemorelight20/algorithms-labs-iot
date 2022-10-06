import sys

from vertex import Vertex, VertexType
from edge import Edge


class Graph:

    @staticmethod
    def dijkstra_algorithm(adjecency_list: dict[Vertex, list[Edge]], start_vertex: Vertex, clients: set[int]):
        unvisited_vertices = adjecency_list.copy()

        distances_from_start = {
            vertex: (0 if vertex == start_vertex else sys.maxsize) for vertex in adjecency_list.keys()
        }

        previous_vertex_store = {vertex: None for vertex in adjecency_list.keys()}

        while unvisited_vertices:
            current_vertex = min(unvisited_vertices, key=lambda vertex: distances_from_start[vertex])
            del unvisited_vertices[current_vertex]

            if distances_from_start[current_vertex] == sys.maxsize:
                break

            for edge in adjecency_list[current_vertex]:
                neighbour = Vertex(VertexType.CLIENT if (edge.to_vertex in clients) else VertexType.ROUTER, edge.to_vertex)
                retention = edge.retention
                new_retention = distances_from_start[current_vertex] + retention
                if new_retention < distances_from_start[neighbour]:
                    distances_from_start[neighbour] = new_retention
                    previous_vertex_store[neighbour] = current_vertex

        return distances_from_start
