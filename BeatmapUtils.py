"""
Data structure
 * X: (ObjectX / 256) - 1
 * Y: (ObjectY / 192) - 1
 * Deltatime: Measured in 1/1 Beats
"""


def circle(raw_hitobject, hitobjects):
    hitobjects.append(','.join(raw_hitobject.split(',')[:4]))


def slider(raw_hitobject, hitobjects):
    split = raw_hitobject.split(',')
    first = ','.join(split[:4])
    second = ','.join(split[5:8])
    hitobjects.append("%s,%s" % (first, second))


def spinner(raw_hitobject, hitobjects):
    split = raw_hitobject.split(',')
    hitobjects.append(','.join(split[:4] + ',%s' % split[-1].split(':')[0]))


def progress_raw_items(raw_hitobjects):
    hitobjects = []

    # Each appends its contents individually
    for raw_hitobject in raw_hitobjects:
        type = raw_hitobject.split(',')[3]
        if type & 1:
            return circle(raw_hitobject, hitobjects)
        elif type & 2:
            return slider(raw_hitobject, hitobjects)
        elif type & 8:
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
