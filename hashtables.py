class HashTables:
    def __init__(self, size=7) -> None:
        self.data_map: list = [None] * size

    def print_table(self) -> None:
        for index, value in enumerate(self.data_map):
            print(f"{index}: {value}")

    def _hash(self, key: str) -> int:
        hash_value = 0
        for letter in key:
            ascii_val = ord(letter)
            hash_value = ((ascii_val + hash_value) * 23) % len(self.data_map)
        return hash_value

    def set(self, key: str, value: int) -> bool:
        index: int = self._hash(key)
        index_list = []
        if self.data_map[index] is not None:
            self.data_map[index].append((key, value))
        else:
            self.data_map[index] = index_list
            index_list.append((key, value))
        return True

    def get(self, key: str) -> int:
        index: int = self._hash(key)
        for key_valu_pair in self.data_map[index]:
            if key_valu_pair[0] == key:
                return key_valu_pair[1]
        return -1

    def get_keys(self):
        result = []
        for rows in self.data_map:
            if rows is not None:
                for index, values in enumerate(rows):
                    print(f"{index}: {values}")
                    result.append(rows[index][0])
        return result


if __name__ == "__main__":
    my_table = HashTables()
    # my_table.print_table()
    print(my_table._hash("nava"))
    my_table.set("nava", 100)
    my_table.set("nava", 200)
    my_table.set("navaneeth", 180)
    my_table.set("ram", 290)
    my_table.print_table()
    print('************')
    # my_table1 = HashTables()
    # # my_table1.print_table()
    # print(my_table1._hash("nava"))
    # my_table1.set("nava", 10)
    # my_table1.set("nava", 20)
    # my_table1.print_table()
    print(my_table.get("navaneeth"))
    print(my_table.get("nava1"))
    print(my_table.get("nava"))
    print()
    print('************')
    print(my_table.get_keys())
