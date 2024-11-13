"""Node Class ICL."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    # Magic method init
    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Rep a Node object as a string"""
        rest: str = "?"
        # overwrites str(object) ouput
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
# print(courses) -> <__main__.Node object at 0xffffb7659490>
# hexadecimal (0xffffb7659490) address in heap (base 16)


def to_str(head: Node | None) -> str:
    """Rep a linked list as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


# print(to_str(one))


def last(head: Node) -> int:
    """Return last value of a Linked List."""
    # If head is followed by None, return head's value
    if head.next is None:
        return head.value  # Base Case
    else:
        last_node: int = last(head.next)  # recursive case
        return last_node


print(last(one))  # expect 2
print(last(courses))  # Expect 301
