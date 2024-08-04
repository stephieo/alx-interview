#!/usr/bin/python3
""" Lockboxes interview question
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each element is a list of keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    openedBoxes = set()
    stackbox = [0]

    while stackbox:
        currentBox = stackbox.pop()
        if currentBox not in openedBoxes:
            openedBoxes.add(currentBox)
            for key in boxes[currentBox]:
                if key < n:
                    stackbox.append(key)

    return len(openedBoxes) == n
