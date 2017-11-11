from db.BasicDbReader import BasicDbReader


class CollectionsDbReader(BasicDbReader):
    def __init__(self, file=None):
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

