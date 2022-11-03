class FileUtils:
    @staticmethod
    def get_data(file_name: str = "wchain.in"):
        with open(file_name) as file:
            words_amount = int(file.readline().strip())
            words = []
            for word in file.readlines():
                words.append(word.strip())

            return words_amount, words

    @staticmethod
    def save_result(content: str, file_name: str = "wchain.out"):
        with open(file_name, "w") as file:
            file.write(content)
