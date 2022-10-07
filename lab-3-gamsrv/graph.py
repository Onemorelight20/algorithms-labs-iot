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

        while unvisited_vertices:
            # from unvisited vertices we choose the one with shortest path
            current_vertex = min(unvisited_vertices, key=lambda vertex: distances_from_start[vertex])
            # mark it as visited
            del unvisited_vertices[current_vertex]

            # iterate through current_vertex neighbours and relaxing retention
            for edge in adjecency_list[current_vertex]:
                neighbour_for_current_vertex = Vertex(VertexType.CLIENT if (edge.to_vertex in clients) else VertexType.ROUTER, edge.to_vertex)
                retention = edge.retention
                new_retention = distances_from_start[current_vertex] + retention
                if new_retention < distances_from_start[neighbour_for_current_vertex]:
                    distances_from_start[neighbour_for_current_vertex] = new_retention

        return distances_from_start
