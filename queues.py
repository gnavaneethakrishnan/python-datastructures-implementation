from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[Node] = None


class Queues:
    def __init__(self, value: int) -> None:
        newNode = Node(value)
        self.first: Optional[Node] = newNode
        self.last: Optional[Node] = newNode
        self.length = 1

    def print_queue(self) -> None:
        temp: Optional[Node] = self.first
        print("First: ", end="")
        while temp is not None:
            print(f"{temp.value}", end=" <- ")
            temp = temp.next
        print(":Last")

    def pop(self) -> Optional[Node]:
        temp: Optional[Node] = self.first
        if self.length == 0:
            return None
        elif self.length == 1:
            self.last = None
            self.first = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp

    def push(self, value: int) -> bool:
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return True


if __name__ == "__main__":
    my_queue = Queues(10)
    # my_queue.push(11)
    # my_queue.push(12)
    # my_queue.push(13)
    # my_queue.push(14)
    # my_queue.push(15)
    print(my_queue.length)
    my_queue.print_queue()
    my_queue.pop()
    # my_queue.pop()
    # my_queue.pop()
    # my_queue.pop()
    # my_queue.pop()
    # my_queue.pop()
    # my_queue.pop()
    print(my_queue.length)
    my_queue.print_queue()
