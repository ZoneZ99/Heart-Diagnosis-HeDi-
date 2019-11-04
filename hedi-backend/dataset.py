import csv
from os.path import join, dirname

import numpy as np


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


def load_dataset(dataset_name: str):
    with open(join(dirname(__file__), 'data', dataset_name)) as csv_file:
        data_file = csv.reader(csv_file)
        header_row = next(data_file)
        number_samples = int(header_row[0])
        number_features = int(header_row[1])
        target_attribute_names = np.array(header_row[2:])
        data_attribute = np.empty(shape=(number_samples, number_features))
        target_attribute = np.empty(shape=(number_samples,), dtype=np.int)

        for index, sample in enumerate(data_file):
            data_attribute[index] = np.asarray(sample[:-1], dtype=np.float64)
            target_attribute[index] = np.asarray(sample[-1], dtype=np.int)

    return data_attribute, target_attribute, target_attribute_names
