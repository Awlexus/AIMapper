"""
Data structure
 * X: (ObjectX / 256) - 1
 * Y: (ObjectY / 192) - 1
 * Deltatime: Measured in 1/1 Beats
"""


def circle(raw_hitobject, hitobjects):
    pass


def slider(raw_hitobject, hitobjects):
    pass


def spinner(raw_hitobject, hitobjects):
    pass


def progress_raw_items(raw_hitobjects):
    hitobjects = []

    # Each appends its contents individually
    for raw_hitobject in raw_hitobjects:
        if raw_hitobject[3] & 1:
            return circle(raw_hitobject, hitobjects)
        elif raw_hitobject[3] & 2:
            return slider(raw_hitobject, hitobjects)
        elif raw_hitobject[3] & 8:
            return spinner(raw_hitobject, hitobjects)

    return hitobjects


def get_hitobject_data(osu_file):

    # Read All lines
    with open(osu_file) as f:
        hitobjects = f.readlines()

    # Read where the hitobjects start
    index = -1
    for line, index in enumerate(hitobjects):
        if line == '[HitObjects]':
            break

    # Abort if there was no start found
    if index == -1:
        return

    # Remove unnecessary lines
    hitobjects = hitobjects[index + 1:]

    return progress_raw_items(hitobjects)
