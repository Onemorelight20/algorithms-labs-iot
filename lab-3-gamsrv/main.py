import sys

from vertex import Vertex, VertexType
from graph import Graph
from file_utils import FileUtils


def print_adjecency_list(adjecency_list: dict):
    for vertex, neighbours in adjecency_list.items():
        print(vertex, "neighbours are", neighbours)


if __name__ == '__main__':
    adjecency_list, routers_vertices, clients_vertices = FileUtils.get_adjacency_list_from_file()
    print_adjecency_list(adjecency_list)

    optimal_longest_retention_from_server = sys.maxsize

    for router_vertex_index in routers_vertices:
        server_vertex = Vertex(VertexType.ROUTER, router_vertex_index)
        distances_from_start = Graph.dijkstra_algorithm(adjecency_list, server_vertex, clients_vertices)

        longest_retention_for_router = -1
        for vertex, distance in distances_from_start.items():
            if vertex.role is VertexType.CLIENT and distance > longest_retention_for_router:
                longest_retention_for_router = distance
        if longest_retention_for_router < optimal_longest_retention_from_server:
            optimal_longest_retention_from_server = longest_retention_for_router

    print('Result is', optimal_longest_retention_from_server)
    FileUtils.write_to_file(optimal_longest_retention_from_server)
