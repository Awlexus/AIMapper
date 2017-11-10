class OsuDB:
    def __init__(self, file=None):
        self.file = open(file)

    def read_byte(self):
        """
        Read one Byte from the database-file
        :param file:
        :return:
        """
        pass

    def read_short(self):
        """
        Read a Short (2 Byte) from the database-file
        :return:
        """
        pass

    def read_int(self):
        """
        Read a Integer (4 Bytes) from the database-file
        :return:
        """
        pass

    def read_long(self):
        """
        Read a Long (8 bytes) from the database-file
        :return:
        """
        pass

    def read_uleb128(self):
        """
        Read a uleb128 (variable) from the database-file
        :return:
        """
        pass

    def read_single(self):
        """
        Read a Single (4 bytes) from the database-file
        :return:
        """
        pass

    def read_double(self):
        """
        Read a Double (8 bytes) from the database-file
        :return:
        """
        pass

    def read_boolean(self):
        """
        Read a Boolean (1 byte) from the database-file
        :return:
        """
        pass

    def read_string(self):
        """
        Read a string (variable) from the database-file
        :return:
        """
        pass


def fetch_n_ranked_maps(n=1000, min_sr=None, max_sr=None, random=True, game_mode='std', use_exported=True,
                        export_list=True,
                        filename='exported_maps.pkl'):
    """

    :param n: number of beatmaps to fetch.
    :param min_sr: lowest star rating
    :param max_sr: highest star rating
    :param random: shuffle entries
    :param use_exported: Use already exported list
    :param export_list: export the query to [filename]
    :param filename: Where to save the exported list
    :return:
    """
    pass
