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


if __name__ == "__main__":
    my_tree: BinarySearchTree = BinarySearchTree()
    print(my_tree.root)
    my_tree.insert__(10)
    my_tree.insert__(11)
    print(my_tree.root.right.value)  # type: ignore
    my_tree.insert__(9)
    my_tree.insert__(12)
    print(my_tree.root.right.right.value)  # type: ignore
