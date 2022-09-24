from vertex import Vertex
from graph import Graph
import utills

def test1():
    file_content = utills.get_file_content_list('input.txt')
    adjecency_list = utills.get_adjecency_list(file_content)

    graph = Graph(adjecency_list)
    path = graph.bfs(Vertex(2,0), Vertex(2,9))
    if path != -1:
        print(len(path))
    print(path)

    utills.write_result_to_file('output.txt', file_content, path)


def test2():
    file_content = utills.get_file_content_list('input1.txt')
    adjecency_list = utills.get_adjecency_list(file_content)

    graph = Graph(adjecency_list)
    path = graph.bfs(Vertex(2, 0), Vertex(6, 9))
    if path != -1:
        print(len(path))
    print(path)

    utills.write_result_to_file('output1.txt', file_content, path)


if __name__ == '__main__':
    #test1()
    test2()
