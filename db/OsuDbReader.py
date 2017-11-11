from db.BasicDbReader import BasicDbReader
import os


class OsuDbReader(BasicDbReader):
    def __init__(self, file=None):
        # Tries to use a default file if the file was not specified or not found
        if not file or not os.path.exists(file):
            file = os.path.join(self.get_default_osu_path(), 'osu!.db')
        super(OsuDbReader, self).__init__(file)
        self.version = self.read_int()
        self.folder_count = self.read_int()
        self.unlocked = self.read_boolean()
        self.date_unlocked = self.read_datetime()
        self.player = self.read_string()
        self.num_beatmaps = self.read_int()

    def read_int_double_pair(self):
        """
        Read an int-double-pair (14 bytes) from the database-file
        :return:
        """
        if self.read_byte() == 0x08:
            first = self.read_int()
            if self.read_byte() != 0x0d:
                return first
            second = self.read_double()
            return first, second

    def read_timingpoint(self):
        """
        Read a Timingpoint (17 bytes) from the database-file
        :return:
        """
        bpm = self.read_double()
        offset = self.read_double()
        inherited = self.read_boolean()

        return {
            'bpm': bpm,
            'offset': offset,
            'inherited': inherited
        }

    def read_beatmap(self):
        """
        Read one Beatmap from the database-file
        :return:
        """
        entry_size = self.read_int()
        artist = self.read_string()
        artist_unicode = self.read_string()
        title = self.read_string()
        title_unicode = self.read_string()
        creator = self.read_string()
        difficulty = self.read_string()
        audio_file = self.read_string()
        md5 = self.read_string()
        osu_file = self.read_string()
        ranked_status = self.read_byte()
        circle_count = self.read_short()
        slider_count = self.read_short()
        spinner_count = self.read_short()
        last_modification_time = self.read_long()
        ar = self.read_single()
        cs = self.read_single()
        hp = self.read_single()
        od = self.read_single()
        slider_velocity = self.read_double()

        # Difficulties in respect with the selected mod
        difficulties_std = []
        difficulties_taiko = []
        difficulties_ctb = []
        difficulties_mania = []

        length = self.read_int()
        for _ in range(length):
            difficulties_std.append(self.read_int_double_pair())

        length = self.read_int()
        for _ in range(length):
            difficulties_taiko.append(self.read_int_double_pair())

        length = self.read_int()
        for _ in range(length):
            difficulties_ctb.append(self.read_int_double_pair())

        length = self.read_int()
        for _ in range(length):
            difficulties_mania.append(self.read_int_double_pair())

        drain_time = self.read_int()
        total_time = self.read_int()
        preview_time = self.read_int()

        # Timingpoints
        timing_points = []
        length = self.read_int()
        for _ in range(length):
            timing_points.append(self.read_timingpoint())

        map_id = self.read_int()
        set_id = self.read_int()
        thread_id = self.read_int()
        grade_std = self.read_byte()
        grade_taiko = self.read_byte()
        grade_ctb = self.read_byte()
        grade_mania = self.read_byte()
        local_offset = self.read_short()
        stack_leniency = self.read_single()
        game_mode = self.read_byte()  # 0x00 = osu!Standard, 0x01 = Taiko, 0x02 = CTB, 0x03 = Mania
        song_source = self.read_string()
        song_tags = self.read_string()
        online_offset = self.read_short()
        font = self.read_string()  # Why do you even need this -_-
        unplayed = self.read_boolean()
        last_played = self.read_long()
        ignore_map_sound = self.read_boolean()
        ignore_map_skin = self.read_boolean()
        disable_storyboard = self.read_boolean()
        disable_video = self.read_boolean()
        visual_override = self.read_boolean()  # I have no idea what that is supposed to be
        last_modification_time_2 = self.read_int()  # I swear we had this already
        mania_scroll_speed = self.read_byte()

        # Don't worry, I used multiply cursors to do within a minute
        return {
            'entry_size': entry_size,
            'artist': artist,
            'artist_unicode': artist_unicode,
            'title': title,
            'title_unicode': title_unicode,
            'creator': creator,
            'difficulty': difficulty,
            'audio_file': audio_file,
            'md5': md5,
            'osu_file': osu_file,
            'ranked_status': ranked_status,
            'circle_count': circle_count,
            'slider_count': slider_count,
            'spinner_count': spinner_count,
            'last_modification_time': last_modification_time,
            'ar': ar,
            'cs': cs,
            'hp': hp,
            'od': od,
            'slider_velocity': slider_velocity,
            'difficulties_std': difficulties_std,
            'difficulties_taiko': difficulties_taiko,
            'difficulties_ctb': difficulties_ctb,
            'difficulties_mania': difficulties_mania,
            'drain_time': drain_time,
            'total_time': total_time,
            'preview_time': preview_time,
            'timing_points': timing_points,
            'map_id': map_id,
            'set_id': set_id,
            'thread_id': thread_id,
            'grade_std': grade_std,
            'grade_taiko': grade_taiko,
            'grade_ctb': grade_ctb,
            'grade_mania': grade_mania,
            'local_offset': local_offset,
            'stack_leniency': stack_leniency,
            'game_mode': game_mode,
            'song_source': song_source,
            'song_tags': song_tags,
            'online_offset': online_offset,
            'font': font,
            'unplayed': unplayed,
            'last_played': last_played,
            'ignore_map_sound': ignore_map_sound,
            'ignore_map_skin': ignore_map_skin,
            'disable_storyboard': disable_storyboard,
            'disable_video': disable_video,
            'visual_override': visual_override,
            'last_modification_time_2': last_modification_time_2,
            'mania_scroll_speed': mania_scroll_speed
        }
