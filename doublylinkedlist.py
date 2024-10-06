from typing import List, Optional


class ListNode:
    def __init__(self, value: int, next_node=None) -> None:
        self.value = value
        self.next: Optional[ListNode] = next_node


class Linked_List:
    # Initializing the list with a dummy node to make removing from the list easier
    def __init__(self) -> None:
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while current is not None:
            if i == index:
                return current.value
            i += 1
            current = current.next
        return -1

    def insert_head(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insert_tail(self, value: int) -> None:
        new_node = ListNode(value)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        i: int = 0
        current: ListNode = self.head
        while i < index and current:
            i += 1
            current = current.next
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True    
        return False

    def get_values(self) -> List[int]:
        current = self.head.next
        result: List[int] = []
        while current:
            result.append(current.value)
            current = current.next
        return result


if __name__ == "__main__":
    print("start")
    my_list = Linked_List()
    print(my_list.get_values())
    print('head: ', my_list.head.value)
    print('tail: ', my_list.tail.value)
    print("***********")

    my_list.insert_head(25)
    my_list.insert_head(24)
    my_list.insert_tail(23)
    my_list.insert_head(22)
    print(my_list.get_values())
    print('head: ', my_list.head.value)
    print('tail: ', my_list.tail.value)

    print("***********")
    my_list.remove(0)
    print(my_list.get_values())
    print('head: ', my_list.head.value)
    print('tail: ', my_list.tail.value)
