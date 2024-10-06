from typing import Optional

from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[Node] = None


class Linked_List:

    def __init__(self, value: int) -> None:
        newNode: Node = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length: int = 1

    def print_linked_list(self):
        temp: Optional[Node] = self.head
        while (temp is not None):
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def append(self, value: int) -> bool:
        newNode: Node = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return True

    def prepend(self, value: int) -> bool:
        newNode: Node = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True

    def pop(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp: Optional[Node] = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            while (temp.next is not None):
                pre: Node = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        return temp

    def pop_first(self) -> Optional[Node]:
        temp: Optional[Node] = self.head
        if self.head is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index: int) -> Optional[Node]:
        if 0 < index or index >= self.length:
            return None
        temp: Optional[Node] = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index: int, value: int) -> bool:
        temp: Node = self.get(index)
        if temp is not None:
            temp.value = value
            return True

    def insert(self, index: int, value: int) -> bool:

        if index < 0 or index > self.length:
            return False

        newNode: Node = Node(value)
        if index == 0:
            self.prepend(value)
            return True

        elif index == self.length:
            self.append(value)
            return True
        else:
            pre: Node = self.get(index-1)
            temp = pre.next
            pre.next = newNode
            newNode.next = temp
            self.length += 1
            return True



    def remove(self, index: int) -> Optional[Node]:
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            pre = self.get(index - 1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return temp
        
    def reverse(self):
        temp: Node = self.head
        self.head, self.tail = self.tail, self.head
        before: Node = None
        after: temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


if __name__ == "__main__":
    my_list_1 = Linked_List(20)
    print(my_list_1.head.value)
    print(my_list_1.tail.value)
    print(my_list_1.length)
    my_list_1.append(25)
    my_list_1.append(30)
    my_list_1.print_linked_list()
    print('head: ', my_list_1.head.value)
    print('tail: ', my_list_1.tail.value)
    print('length: ', my_list_1.length)
    my_list_1.prepend(5)
    my_list_1.prepend(15)
    print('head: ', my_list_1.head.value)
    print('tail: ', my_list_1.tail.value)
    print('length: ', my_list_1.length)
    my_list_1.print_linked_list()
    print("***********")
    my_list_1.pop()
    print('head: ', my_list_1.head.value)
    print('tail: ', my_list_1.tail.value)
    print('length: ', my_list_1.length)
    my_list_1.print_linked_list()
    """ print("***********")
    my_list_1.pop()
    print('head: ', my_list_1.head.value)
    print('tail: ', my_list_1.tail.value)
    print('length: ', my_list_1.length)
    my_list_1.print_linked_list()
    print("***********")
    my_list_1.pop()
    print('head: ', my_list_1.head.value)
    print('tail: ', my_list_1.tail.value)
    print('length: ', my_list_1.length)
    my_list_1.print_linked_list()
    print("***********")
    my_list_1.pop()
    print('head: ', my_list_1.head.value)
    print('tail: ', my_list_1.tail.value)
    print('length: ', my_list_1.length)
    my_list_1.print_linked_list()
    print("***********")
    my_list_1.pop()
    print('head: ', my_list_1.head.value)
    print('tail: ', my_list_1.tail.value)
    print('length: ', my_list_1.length)
    my_list_1.print_linked_list() """
    print(my_list_1.get(3).value)
    print(my_list_1.get(2).value)
    print(my_list_1.get(1).value)
    print(my_list_1.get(0).value)
    my_list_1.set(3, 100)
    my_list_1.print_linked_list()
    print(my_list_1.get(3).value)
    my_list_1.insert(1, 200)
    my_list_1.print_linked_list()
    print(my_list_1.remove(1).value)
    my_list_1.print_linked_list()
    print('head: ', my_list_1.head.value)
    print('tail: ', my_list_1.tail.value)
    print('length: ', my_list_1.length)
    my_list_1.reverse()
    my_list_1.print_linked_list()
    print('head: ', my_list_1.head.value)
    print('tail: ', my_list_1.tail.value)
    print('length: ', my_list_1.length)
    

        