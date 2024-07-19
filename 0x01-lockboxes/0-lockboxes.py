#!/usr/bin/python3

"""
Module: 0-lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): A list of lists
        where each list contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]  # Start with the key to the first box

    while keys:
        key = keys.pop()
        for new_key in boxes[key]:
            if new_key < n and not unlocked[new_key]:
                unlocked[new_key] = True
                keys.append(new_key)

    return all(unlocked)
