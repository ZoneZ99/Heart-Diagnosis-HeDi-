import numpy as np

class DecisionTreeClassifier:

    def __init__(self, dataset, max_depth):
        self.dataset = dataset
        self.depth = 0
        self.max_depth = max_depth

    def find_best_split(self, split_column, target_variable):
        min_entropy = 10
        n = len(target_variable)

        for value in set(split_column):
            y_predict = split_column < value
            entropy = get_entropy(y_predict, target_variable)
            if entropy <= min_entropy:
                min_entropy = entropy
                cutoff = value
        return min_entropy, cutoff