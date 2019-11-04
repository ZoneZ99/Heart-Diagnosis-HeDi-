import csv
from os.path import join


class DatasetContainer(dict):

    def __init__(self, **kwargs):
        super(DatasetContainer, self).__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(item)

    def __dir__(self):
        return self.keys()
