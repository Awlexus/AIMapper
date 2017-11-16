import os
import pprint

import pandas as pd

from PyOsuDBReader.pyosudbreader import get_default_osu_path


def prepare_data(map_list, filename):
    # Make parent directories
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename), 777)

    # Read data
    df = pd.read_csv(map_list, delimiter='\t')  # Make paths absolute
    osu_path = get_default_osu_path()
    df['folder_name'] = osu_path + os.sep + df['folder_name']
    df['osu_file'] = df['folder_name'] + os.sep + df['osu_file']
    df['audio_file'] = df['folder_name'] + os.sep + df['audio_file']
    df.drop('folder_name', axis=1, inplace=True)

    # Write TrainingData
    df.count(axis=1)
    df.iloc[:, :5].apply(lambda data: pprint.pprint(data))


if __name__ == '__main__':
    prepare_data('map_list/easy_ranked.csv', 'data/easy_ranked.pkl')
