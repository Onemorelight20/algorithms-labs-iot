from edge import Edge
from vertex import Vertex, VertexType


class FileUtils:
    @staticmethod
    def get_adjacency_list_from_file(file_name: str = "gamsrv.in"):
        with open(file_name) as file:
            vertex_count, edges_count = [int(num) for num in file.readline().strip().split()]
            clients_vertices = set((int(index) for index in file.readline().strip().split()))
            routers_vertices = set()

            print('Client vertices', clients_vertices)
            edges = []
            for line in file.readlines():
                line = line.strip()
                start_vertex, end_vertex, retention = [int(num) for num in line.split()]
                edges.append(Edge(start_vertex, end_vertex, retention))
                edges.append(Edge(end_vertex, start_vertex, retention))
            print("Edges are", edges)
            adjecency_list = {}

            for vertex_index in range(1, vertex_count + 1):
                if vertex_index in clients_vertices:
                    vertex = Vertex(VertexType.CLIENT, vertex_index)
                    adjecency_list[vertex] = []
                else:
                    vertex = Vertex(VertexType.ROUTER, vertex_index)
                    routers_vertices.add(vertex_index)
                    adjecency_list[vertex] = []

            print('Router vertices are', routers_vertices)
            for vertex, neighbours_list in adjecency_list.items():
                vertex_index = vertex.index
                for edge in edges:
                    if edge.from_vertex is vertex_index and edge not in adjecency_list[vertex]:
                        adjecency_list[vertex].append(edge)

            return adjecency_list, routers_vertices, clients_vertices

    @staticmethod
    def write_to_file(content: str, file_name: str = "gamsrv.out"):
        with open(file_name, "w") as file:
            file.write(str(content))



