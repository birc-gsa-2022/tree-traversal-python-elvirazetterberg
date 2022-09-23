"""A module for breadth-first traversal of trees."""

from collections import deque
from typing import Iterable
from tree import T


def bf_order(t: T | None) -> Iterable[int]:
    """Breadth-first traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(bf_order(tree))
    [2, 1, 4, 3, 5]
    """

    queue = deque()


    # end when all leaves to the right are None.

    # append values to res list until the stack is empty
    res = []
    queue.append(t)

    while True:
        if len(queue) > 0:
            t = queue.popleft()
            res.append(t.val)
        else:
            break
        if t.left:
            queue.append(t.left)
        if t.right:
            queue.append(t.right)

    return res

    
# def main():
#     tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
#     print(list(bf_order(tree)))

# if __name__ == '__main__':
#     main()