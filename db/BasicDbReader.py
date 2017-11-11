import struct
import os


class BasicDbReader:
    def __init__(self, file=None):
        if not file or not os.path.exists(file):
            raise FileNotFoundError('Could not read from the specified file "%s"' % file)
        self.file = open(file, mode='rb', encoding='utf8')

    def read_byte(self):
        """
        Read one Byte from the database-file
        :param file:
        :return:
        """
        return int.from_bytes(self.file.read(1), byteorder='little')

    def read_short(self):
        """
        Read a Short (2 Byte) from the database-file
        :return:
        """
        return int.from_bytes(self.file.read(2), byteorder='little')

    def read_int(self):
        """
        Read an Integer (4 Bytes) from the database-file
        :return:
        """
        return int.from_bytes(self.file.read(4), byteorder='little')

    def read_long(self):
        """
        Read a Long (8 bytes) from the database-file
        :return:
        """
        return int.from_bytes(self.file.read(8), byteorder='little')

    def read_uleb128(self):
        """
        Read a ULEB128 (variable) from the database-file
        :return:
        """
        result = 0
        shift = 0
        while True:
            byte = int.from_bytes(self.file.read(1), byteorder='little')
            result |= ((byte & 127) << shift)
            if (byte & 128) == 0:
                break
            shift += 7
        return result

    def read_single(self):
        """
        Read a Single (4 bytes) from the database-file
        :return:
        """
        return struct.unpack('f', self.file.read(4))

    def read_double(self):
        """
        Read a Double (8 bytes) from the database-file
        :return:
        """
        return struct.unpack('d', self.file.read(8))

    def read_boolean(self):
        """
        Read a Boolean (1 byte) from the database-file
        :return:
        """
        return self.read_byte() is not 0

    def read_string(self):
        """
        Read a string (variable) from the database-file
        :return:
        """
        if self.read_byte() is 0x0b:
            len = self.read_uleb128()
            return self.file.read(len).decode('utf8')

    def read_datetime(self):
        """
        Read a Datetime from the database-file
        :return:
        """
        pass

