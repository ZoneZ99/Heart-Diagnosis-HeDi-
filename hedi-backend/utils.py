import bisect
import os
import random
from statistics import mean

identity = lambda x: x
argmax = max


def num_or_str(entity):
    try:
        return int(entity)
    except ValueError:
        try:
            return float(entity)
        except ValueError:
            return str(entity).strip()


def mean_boolean_error(X, Y):
    return mean(
        int(x != y)
        for x, y in zip(X, Y)
    )


def remove_all(item, sequence):
    if isinstance(sequence, str):
        return sequence.replace(item, '')
    else:
        return [
            x for x in sequence
            if x != item
        ]


def unique(sequence):
    return list(set(sequence))


def argmax_random_tie(sequence, key=identity):
    return argmax(shuffled(sequence), key=key)


def shuffled(iterable):
    items = list(iterable)
    random.shuffle(items)
    return items


def normalize(distribution):
    if isinstance(distribution, dict):
        total = sum(distribution.values())
        for key in distribution:
            distribution[key] = distribution[key] / total
            assert 0 <= distribution[key] <= 1, "Probabilities must be between 0 and 1."
        return distribution
    total = sum(distribution)
    return [
        (n / total) for n in distribution
    ]


def weighted_sample_with_replacement(n, sequence, weights):
    sample = weighted_sampler(sequence, weights)
    return [sample() for _ in range(n)]


def weighted_sampler(sequence, weights):
    totals = []
    for w in weights:
        totals.append(
            w + totals[-1]
            if totals
            else w
        )
    return lambda: sequence[bisect.bisect(totals, random.uniform(0, totals[-1]))]


def open_data(name, mode='r'):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = os.path.join(root, *['cardiovascular-disease-dataset', name])
    return open(file, mode=mode)


def parse_csv(csv, delimiter=','):
    lines = [
        line for line in csv.splitlines()
        if line.strip()
    ]
    return [
        list(
            map(
                num_or_str, line.split(delimiter)
            )
        )
        for line in lines
    ]
