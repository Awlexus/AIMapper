import os

from PyOsuDBReader.pyosudbreader import OsuDbReader


def query_maps(min_sr=0, max_sr=10, ranked=None, mode=0, mods=0, verbose=False):
    """
    Query the db for beatmaps matching the given parameters

    :param min_sr: lower border for star rating
    :param max_sr: higher border for star rating
    :param ranked: ranked status. None means all are allowed
    :param mode: gamemode for this map. None mean all are allowed
    :param mods: which mods should be active
    :param verbose: Print the current state
    :return: A list of maps the match the given criteria
    """
    if verbose:
        print('Loading Beatmaps...')
    mode = {
        0: 'difficulties_std',
        1: 'difficulties_taiko',
        2: 'difficulties_ctb',
        3: 'difficulties_mania',
    }.get(mode)
    with OsuDbReader() as db:
        db.read_all_beatmaps()
    if verbose:
        print('Beatmaps loaded.\nApplying filters:\n\tmin_sr= {:2.2f}\n\tmax_sr= {:2.2f}\n\tranked={:2}'
              .format(min_sr, max_sr, ranked))

    map_list = [beatmap for beatmap in db.beatmaps
                if beatmap[mode]
                and (ranked or beatmap['ranked_status'] == ranked)
                and min_sr <= beatmap[mode][mods] <= max_sr
                ]
    if verbose:
        print('Beatmaps filtered. {0} Matches'.format(len(map_list)))

    return map_list


def save_maps(beatmaps, map_attributes, filename):
    """
    Saves the given attributes into a .csv file

    :param beatmaps: List of maps
    :param map_attributes: which attributes should be saved
    :param filename: where should the attributes be saved
    """
    if not beatmaps or not map_attributes or not filename:
        return

    # Make parent directories
    index = filename.rfind(os.sep)
    if index == -1:
        index = 0
    os.makedirs(filename[:index], 777)

    with open(filename, 'w+', encoding='utf8') as file:

        # Write attribute names as headers
        for index, map_attribute in enumerate(map_attributes):
            file.write(map_attribute)
            file.write('\t' if index < len(map_attributes) - 1 else '\n')

        # Write all attributes
        for beatmap in beatmaps:
            for index, map_attribute in enumerate(map_attributes):
                file.write(beatmap[map_attribute])
                file.write('\t' if index < len(map_attributes) - 1 else '\n')


if __name__ == '__main__':
    # For testing purposes
    maps = query_maps(ranked=2, min_sr=1, max_sr=2)
    attributes = ['folder_name', 'osu_file', 'audio_file']
    save_maps(maps, attributes, os.path.join('map_list', 'easy_ranked.csv'))
