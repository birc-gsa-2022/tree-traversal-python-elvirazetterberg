"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable
from tree import T
from collections import deque


def in_order(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order(tree))
    [1, 2, 3, 4, 5]
    """

    # # recursive
    # if t == None:
    #     return
    # else:
    #     return [in_order(t.left), t.val, in_order(t.right)]
    
    stack = deque()
    res = deque()
    # append values to res list until the stack is empty
    while True:
        while t != None:
            stack.append(t)
            t = t.left
        if len(stack) > 0:
            t = stack.pop()
            res.append(t.val)
            t = t.right
        else:
            break

    return res


# def main():
#     tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
#     print(list(in_order(tree)))

# if __name__ == '__main__':
#     main()