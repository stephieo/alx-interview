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

# Example usage:
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 2], [0, 3], [1, 4], [2], [3]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 2, 3], [3, 0, 1], [2], [0]]
print(canUnlockAll(boxes))  # False
