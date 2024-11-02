from typing import Optional


class Node:

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinarySearchTree:

    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert__(self, value: int) -> bool:
        new_node: Node = Node(value)
        if self.root == None:
            self.root = new_node
            return True

        temp: Optional[Node] = self.root

        while (True):
            if temp is not None and temp.value == new_node.value:
                return False
            if temp is not None and new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp is not None and temp.right == None:
                    temp.right = new_node
                    return True
                if temp is not None:
                    temp = temp.right

    def contains__(self, value: int) -> bool:
        temp: Optional[Node] = self.root
        while True:
            if temp is None:
                return False
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True

    def __r_contains(self, current_node: Node, value: int) -> bool:

        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        elif value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value: int) -> bool:
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node: Node, value: int) -> None | Node:

        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def minimum_value(self, current_node: Node) -> int:
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_(self, current_node: Node, value: int) -> Node | None:

        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                min_value = self.minimum_value(current_node.right)
                current_node.value = min_value
                current_node.right = self.__delete_(current_node.right, min_value)
        return current_node

    def delete(self, value: int) -> Node | None:
        if self.root is None:
            return None
        return self.__delete_(self.root, value)


if __name__ == "__main__":
    my_tree: BinarySearchTree = BinarySearchTree()
    print(my_tree.root)
    my_tree.r_insert(10)
    print(my_tree.root.value)
    my_tree.r_insert(11)
    print(my_tree.root.right.value)
    my_tree.insert__(9)
    my_tree.insert__(12)
    print(my_tree.root.right.right.value)  # type: ignore
