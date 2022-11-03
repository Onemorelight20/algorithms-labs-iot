class Wchain:

    @staticmethod
    def get_words_grouped_by_len_dict(words: list[str]) -> dict[str:list[str]]:
        sorted_words = sorted(words, key=lambda wrd: len(wrd), reverse=True)
        words_grouped_by_len_dict = {}

        for word in sorted_words:
            len_key = len(word)
            if len_key in words_grouped_by_len_dict:
                words_grouped_by_len_dict[len_key].append(word)
            else:
                words_grouped_by_len_dict[len_key] = [word]
        return words_grouped_by_len_dict

    @staticmethod
    def get_suitable_words(curr_word, shorter_words_list) -> list[str]:
        possible_variants = Wchain.get_suitable_next_step_words(curr_word)
        suitable_next_words = []
        for word in shorter_words_list:
            if word in possible_variants:
                suitable_next_words.append(word)
        return suitable_next_words

    @staticmethod
    def get_suitable_next_step_words(word: str) -> set[str]:
        possible_variants = set()
        for idx_to_remove in range(len(word)):
            possible_variants.add(word[:idx_to_remove] + word[idx_to_remove + 1:])
        return possible_variants
