from file_utils import FileUtils

if __name__ == '__main__':
    words_amount, words = FileUtils.get_data()
    sorted_words = sorted(words, key=lambda word: len(word), reverse=True)

    print("Amount of words", words_amount)
    print("Words", words)
    print("Sorted words", sorted_words)

    absolute_maximum = 0
    local_maximum = 0

    buffer_word = sorted_words.pop(0)
    for curr_word in sorted_words:
        print("curr_word >>",curr_word)
        if curr_word == buffer_word[:-1] or curr_word == buffer_word[1:]:
            local_maximum += 1
            if local_maximum > absolute_maximum:
                absolute_maximum = local_maximum
        else:
            local_maximum = 1
        buffer_word = sorted_words.pop(0)

    print(absolute_maximum)

