from db.OsuDbReader import OsuDbReader
import pprint

db_reader = OsuDbReader()

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
