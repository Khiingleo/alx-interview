#!/usr/bin/python3
""" lockbox algorithm """


def canUnlockAll(boxes):
    """ function that determines if all boxes can be unlocked """
    num_boxes = len(boxes)

    open_boxes = [False] * num_boxes
    open_boxes[0] = True
    keys = [0]

    while keys:
        current_box = keys.pop()

        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not open_boxes[key]:
                open_boxes[key] = True
                keys.append(key)

    return all(open_boxes)
