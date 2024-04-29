#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""

from collections import deque

def canUnlockAll(boxes):
    """Determines if boxes can be unlocked"""

    n = len(boxes)
    keys = deque([0])
    open = set()

    while keys and len(open) < n:
        key = keys.popleft()
        open.add(key)

        for i in range(len(boxes[key])):
            if i not in open:
                keys.append(i)

    return len(open) == n

