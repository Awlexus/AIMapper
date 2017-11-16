import os

import pandas as pd

from PyOsuDBReader.pyosudbreader import get_default_osu_path


def prepare(map_list, output):
    # if output directory does not exist, we create it
    if not os.path.exists(output):
        os.makedirs(output)

    # Read data
    df = pd.read_csv(map_list, delimiter='\t')

    # Make paths absolute
    osu_path = get_default_osu_path()
    df['folder_name'] = osu_path + os.sep + df['folder_name']
    df['osu_file'] = df['folder_name'] + os.sep + df['osu_file']
    df['audio_file'] = df['folder_name'] + os.sep + df['audio_file']
    df.drop('folder_name', axis=1, inplace=True)


if __name__ == '__main__':
    prepare("map_list/easy_ranked.csv", "data/easy_ranked")
