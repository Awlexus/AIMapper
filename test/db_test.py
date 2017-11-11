import os
from db.OsuDbReader import OsuDbReader
import pprint

osu_path = os.path.join(os.getenv('LOCALAPPDATA'), 'osu!')  # Replace

db_path = os.path.join(osu_path, 'osu!.db')

db_reader = OsuDbReader(db_path)

print('''
version: %i
folder_count: %i
unlocked: %s
date_unlocked: %s
player: %s
number of beatmaps: %i
''' % (db_reader.version, db_reader.folder_count, db_reader.unlocked, db_reader.date_unlocked, db_reader.player,
       db_reader.num_beatmaps))

pprint.pprint(db_reader.read_beatmap())
