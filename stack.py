from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


class stacks:
    def __init__(self, value: int) -> None:
        newNode = Node(value)
        self.top = newNode
        self.height = 1

    def print_stack(self):
        temp: Optional[Node] = self.top
        print("Top")
        while (temp is not None):
            print(f"{temp.value}" "\n⬇︎")
            temp = temp.next

    def push(self, value: int) -> bool:
        newNode: Optional[Node] = Node(value)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.height += 1
        return True

    def pop(self) -> Optional[Node]:

        temp: Optional[Node] = self.top
        if self.top is None:
            return None

        elif self.height == 1:
            self.top = None
            return temp
        else:
            self.top = self.top.next
            temp.next = None

        self.height -= 1
        return temp


if __name__ == "__main__":
    my_stack = stacks(10)
    my_stack.push(11)
    my_stack.push(12)
    my_stack.push(13)
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.print_stack()
