from db.BasicDbReader import BasicDbReader
import os

class ScoreDbReader(BasicDbReader):
    def __init__(self, file=None):
        # Tries to use a default file if the file was not specified or not found
        if not file or not os.path.exists(file):
            file = os.path.join(self.get_default_osu_path(), 'scores.db')
        super(ScoreDbReader, self).__init__(file)
        self.version = self.read_int()
        self.maps_count = self.read_int()

    def read_beatmap(self):
        md5 = self.read_string()
        score_count = self.read_int()
        scores = []
        for _ in range(score_count):
            scores.append(self.read_score())

        return {
            'md5': md5,
            'score_count': score_count,
            'scores': scores
        }

    def read_score(self):
        game_mode = self.read_byte()
        version = self.read_int()
        md5_beatmap = self.read_string()
        player = self.read_string()
        md5_replay = self.read_string()
        num_perfect = self.read_short()
        num_good = self.read_short()
        num_bad = self.read_short()
        num_geki = self.read_short()
        num_katus = self.read_short()
        num_miss = self.read_short()
        score_value = self.read_int()  # smh, still using integer
        max_combo = self.read_short()
        perfect = self.read_boolean()
        mods = self.read_boolean()
        unknown_empty = self.read_string()  # smh
        timestamp = self.read_long()
        unknown_minus_1 = self.read_int()
        online_score_id = self.read_long()

        return {
            'game_mode': game_mode,
            'version': version,
            'md5_beatmap': md5_beatmap,
            'player': player,
            'md5_replay': md5_replay,
            'num_perfect': num_perfect,
            'num_good': num_good,
            'num_bad': num_bad,
            'num_geki': num_geki,
            'num_katus': num_katus,
            'num_miss': num_miss,
            'score_value': score_value,
            'max_combo': max_combo,
            'perfect': perfect,
            'mods': mods,
            'unknown_empty': unknown_empty,
            'timestamp': timestamp,
            'unknown_minus_1': unknown_minus_1,
            'online_score_id': online_score_id
        }

    # Todo: Add a function to query

