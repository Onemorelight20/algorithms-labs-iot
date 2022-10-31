from file_utils import FileUtils
from wchain import Wchain
from graph import Graph

if __name__ == '__main__':
    words_amount, words = FileUtils.get_data()
    words_grouped_by_len_dict = Wchain.get_words_grouped_by_len_dict(words)

    print("Amount of words", words_amount)
    print("Words grouped by length dictionary", words_grouped_by_len_dict)

    longest_path_list = []
    adj_list = {}
    for curr_length, words_of_curr_length in words_grouped_by_len_dict.items():
        for curr_word in words_of_curr_length:
            words_of_smaller_length = words_grouped_by_len_dict.get(curr_length - 1, [])
            possible_moves = Wchain.get_suitable_words(curr_word, words_of_smaller_length)
            adj_list[curr_word] = possible_moves

    mine_graph = Graph(adj_list)
    for adj_list_key in adj_list.keys():
        longest_path_for_curr_key = mine_graph.bfs(adj_list_key)
        if len(longest_path_for_curr_key) > len(longest_path_list):
            longest_path_list = longest_path_for_curr_key

    str_path = " -> ".join(longest_path_list)
    number_of_moves = len(longest_path_list)
    print("Result is", str_path)
    print("Max number of moves is", number_of_moves)
    FileUtils.save_result(str(number_of_moves))
    



