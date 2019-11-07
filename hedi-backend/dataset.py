import csv
import math
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


def load_cardio_dataset():
    data, target, target_names = load_dataset('cardio.csv')
    return DatasetContainer(
        data=data,
        target=target,
        target_names=target_names,
        feature_names=[
            'Age (days)',
            'Gender (F/M)',
            'Height (cm)',
            'Weight (kg)',
            'Systolic Blood Pressure',
            'Diastolic Blood Pressure',
            'Cholesterol (normal/above normal/high)',
            'Glucose (normal/above normal/high)',
            'Smoking (Yes/No)',
            'Alcohol Intake (Yes/No)',
            'Physical Activity (Yes/No)',
        ]
    )


def train_test_split(dataset: DatasetContainer, test_size: float):
    assert len(dataset.data) == len(dataset.target), \
        "Number of data and target should be the same."

    dataset_length = len(dataset.data)
    test_length = math.floor(test_size * len(dataset.data))

    x_train, y_train = dataset.data[:dataset_length - test_length], dataset.target[:dataset_length - test_length]
    x_test, y_test = dataset.data[dataset_length - test_length:], dataset.target[dataset_length - test_length:]
    return x_train, x_test, y_train, y_test