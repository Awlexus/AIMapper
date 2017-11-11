from db.BasicDbReader import BasicDbReader
import os

class CollectionsDbReader(BasicDbReader):
    def __init__(self, file=None):
        # Tries to use a default file if the file was not specified or not found
        if not file or not os.path.exists(file):
            file = os.path.join(self.get_default_osu_path(), 'collection.db')
        super(CollectionsDbReader, self).__init__(file)
        self.version = self.read_int()
        self.num_collections = self.read_int()

    def read_collection(self):
        name = self.read_string()
        num_maps = self.read_int()
        md5_hashes = []

        for _ in range(num_maps):
            md5_hashes.append(self.read_string())

        return {
            'name': name,
            'num_maps': num_maps,
            'md5_hashes': md5_hashes
        }

    # Todo: Add a function to query

