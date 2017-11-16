"""
Data structure
 * X: (ObjectX / 256) - 1
 * Y: (ObjectY / 192) - 1
 * Deltatime: Measured in 1/1 Beats
"""


def _circle(raw_hitobject, hitobjects):
    hitobjects.append(','.join(raw_hitobject.split(',')[:4]))


def _slider(raw_hitobject, hitobjects):
    split = raw_hitobject.split(',')
    split[7] = str(int(round(float(split[7]))))
    first = ','.join(split[:4])
    second = ','.join(split[5:8])
    hitobjects.append("%s,%s" % (first, second))


def _spinner(raw_hitobject, hitobjects):
    split = raw_hitobject.split(',')
    hitobjects.append(','.join(split[:4] + ',%s' % split[-1].split(':')[0]))


def progress_raw_items(raw_hitobjects):
    hitobjects = []

    # Each appends its contents individually
    for raw_hitobject in raw_hitobjects:
        _type = int(raw_hitobject.split(',')[3])
        if _type & 1:
            _circle(raw_hitobject, hitobjects)
        elif _type & 2:
            _slider(raw_hitobject, hitobjects)
        elif _type & 8:
            _spinner(raw_hitobject, hitobjects)

    return hitobjects


def get_hitobject_data(osu_file):
    # Read All lines
    with open(osu_file, encoding='utf8') as f:
        hitobjects = f.readlines()

    # Read where the hitobjects start
    index = -1
    for index, line in enumerate(hitobjects):
        if line.__contains__('[HitObjects]'):
            break

    # Abort if there was no start found
    if not -1 < index < len(hitobjects):
        return

    # Remove unnecessary lines
    hitobjects = hitobjects[index + 1:]

    return progress_raw_items(hitobjects)

