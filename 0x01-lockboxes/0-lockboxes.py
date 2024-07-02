#!/usr/bin/python3
"""function to determine if boxes can be opened"""

def canUnlockAll(boxes):
    if not boxes:
        return False

    unlocked_boxes = set([0])
    keys = set(boxes[0])
    found_new_box = True

    while found_new_box:
        found_new_box = False
        new_keys = set()
        for key in keys:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.add(key)
                new_keys.update(boxes[key])
                found_new_box = True
        keys.update(new_keys)
    
    return len(unlocked_boxes) == len(boxes)