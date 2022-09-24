from vertex import Vertex
from graph import Graph
import utills

if __name__ == '__main__':
    file_content = utills.get_file_content_list('input.txt')
    adjecency_list = utills.get_adjecency_list(file_content)

    graph = Graph(adjecency_list)
    path = graph.bfs(Vertex(2,0), Vertex(0,9))
    if path != -1:
        print(len(path))
    print(path)

    utills.write_result_to_file('output.txt', file_content, path)

