class Basic_hash_table:
    def __init__(self) -> None:
        self.list = [None] * 40

    def __get_index(self, key: str, valide: bool) -> int:
        resulte = 0
        for char in key:
            resulte += ord(char)
        index = resulte % len(self.list)
        if valide:
            return self.__get_valid_index(key, index)
        else:
            return index

    def __get_valid_index(self, key, index):
        while True:
            item = self.list[index]
            if item == None:
                return index
            if item[0] == key:
                return index
            index += 1
            if index == len(self.list) - 1:
                index = 0

    def delete(self, key):
        def delete_next(index):
            word1, word2 = self.list[index], self.list[index + 1]
            if word1 == None or word2 == None:
                return index
            if self.__get_index(word1[0], False) != self.__get_index(word2[0], False):
                return index
            self.list[index] = self.list[index + 1]
            highest_index = delete_next(index + 1)
            return highest_index

        index = self.__get_index(key, True)
        highest_index = delete_next(index)
        self.list[highest_index] = None

    def insert(self, key, value):
        """Insert a new key-value pair"""
        self.list[self.__get_index(key, True)] = (key, value)  # type: ignore (VSCode gibt einen Error den es nicht gibt)

    def find_print(self, key):
        """Find the value associated with a key"""
        # return self.list[self.__get_index(key)]
        print(self.list[self.__get_index(key, True)])

    def update(self, key, value):
        """Change the value associated with a key"""
        self.list[self.__get_index(key, True)] = (key, value)  # type: ignore (VSCode gibt einen Error den es nicht gibt)

    def list_all(self):
        """List all the keys"""
        return [item[0] for item in self.list if item is not None]


if __name__ == "__main__":
    table = Basic_hash_table()
    list = ["list", "istl", "stli", "tlis"]
    for i in list:
        table.insert(i, i[0])
    table.delete("list")
    for i in list:
        table.find_print(i)
    print("Hallo")
