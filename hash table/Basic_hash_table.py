class Basic_hash_table:
    def __init__(self) -> None:
        self.list = [None] * 4096

    def __get_index(self, key: str) -> int:
        resulte = 0
        for char in key:
            resulte += ord(char)
        return resulte % len(self.list)

    def insert(self, key, value):
        """Insert a new key-value pair"""
        self.list[self.__get_index(key)] = (key, value)  # type: ignore (VSCode gibt einen Error den es nicht gibt)

    def find(self, key):
        """Find the value associated with a key"""
        return self.list[self.__get_index(key)]

    def update(self, key, value):
        """Change the value associated with a key"""
        self.list[self.__get_index(key)] = (key, value)  # type: ignore (VSCode gibt einen Error den es nicht gibt)

    def list_all(self):
        """List all the keys"""
        return [item[0] for item in self.list if item is not None]


if __name__ == "__main__":
    table = Basic_hash_table()
    table.insert("Fabian", "Ich bin der Owner")
    print(table.find("Fabian"))
    table.update("Fabian", "hallo")
    print(table.find("Fabian"))
    table.insert("sdfjkdlf", "sjdfklsdf")
    print(table.list_all())
