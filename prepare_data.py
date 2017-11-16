import os
import pprint

import librosa
import pandas as pd

from BeatmapUtils import get_hitobject_data
from PyOsuDBReader.pyosudbreader import get_default_osu_path


def prepare_data(map_list, filename):
    # Make parent directories
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename), 777)

    # Read data
    df = pd.read_csv(map_list, delimiter='\t')  # Make paths absolute
    osu_path = get_default_osu_path()
    df['folder_name'] = osu_path + os.sep + 'songs/' + df['folder_name']
    df['osu_file'] = df['folder_name'] + os.sep + df['osu_file']
    df['audio_file'] = df['folder_name'] + os.sep + df['audio_file']
    df.drop('folder_name', axis=1, inplace=True)

    # Write TrainingData
    data = {
        'song_name': [],
        'text_data': [],
        'image_data': []
    }

    def appendRowData(row):
        data['song_name'] = row['osu_file']
        data['text_data'].append('\n'.join(get_hitobject_data(row['osu_file'])))
        file_ = row['audio_file']
        load, sr = librosa.load(file_)
        beat = librosa.frames_to_time(librosa.beat.beat_track(load)[1], sr=sr)
        data['image_data'].append(beat)

    df.iloc[5:6].apply(axis=1, func=lambda row: appendRowData(row))

    pprint.pprint(data)


if __name__ == '__main__':
    prepare_data('map_list/easy_ranked.csv', 'data/easy_ranked.pkl')
