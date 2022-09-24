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

    res = deque()

    if t != None:
        queue.append(t)

        while queue:
            t = queue.popleft()
            res.append(t.val)
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