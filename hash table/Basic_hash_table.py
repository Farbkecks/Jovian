class Basic_hash_table:
    def __init__(self) -> None:
        self.list = [None] * 4096

    def __get_index(self, key: str) -> int:
        resulte = 0
        for char in key:
            resulte += ord(char)
        index = resulte % len(self.list)
        return self.get_valid_index(key, index)

    def get_valid_index(self, key, index):
        while True:
            item = self.list[index]
            if item == None:
                return index
            if item[0] == key:
                return index
            index += 1
            if index == len(self.list) - 1:
                index = 0

    def insert(self, key, value):
        """Insert a new key-value pair"""
        self.list[self.__get_index(key)] = (key, value)  # type: ignore (VSCode gibt einen Error den es nicht gibt)

    def find_print(self, key):
        """Find the value associated with a key"""
        # return self.list[self.__get_index(key)]
        print(self.list[self.__get_index(key)])

    def update(self, key, value):
        """Change the value associated with a key"""
        self.list[self.__get_index(key)] = (key, value)  # type: ignore (VSCode gibt einen Error den es nicht gibt)

    def list_all(self):
        """List all the keys"""
        return [item[0] for item in self.list if item is not None]


if __name__ == "__main__":
    table = Basic_hash_table()
    table.insert("Fabian", "Ich bin der Owner")
    table.insert("listen", "1")
    table.insert("silent", "2")
    table.find_print("listen")
    table.find_print("silent")
