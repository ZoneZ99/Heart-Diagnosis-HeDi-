# Module for main logic of the app

import math
from os.path import dirname

import numpy as np
from sklearn.datasets.base import load_data


def entropy_formula(class_number, group_number):
    return -(class_number*1.0/group_number) * math.log2(class_number*1.0/group_number)


def entropy_calculation(class1,class2):
    group_number = class1 +class2
    if class1 > 0  and class2 >0:
        return entropy_formula(class1, group_number)+entropy_formula(class2,group_number)
    return 0

def entropy_one_division(division):
    sum_entropy = 0
    num_of_division = len(division)
    classess = set(division)

    for clas in classess:
        sum_entropy += sum(division == clas)*1.0/num_of_division * entropy_calculation(sum(division == clas ),sum(division != clas))
    return sum_entropy, num_of_division

def get_entropy(y_predict, y_real):

    n = len(y_real)
    s_true, n_true = entropy_one_division(y_real[y_predict])
    s_false, n_false = entropy_one_division(y_real[~y_predict])
    return  n_true*1.0/n*s_true + n_false*1.0/n*s_false

def can_be_added_to_queue(tree):
    has_children = tree.get('left') is not None or tree.get('right') is not None
    has_sub_trees = not tree.get('left')['IsLeafNode'] and not tree.get('right')['IsLeafNode']
    return tree is not None and has_children  and has_sub_trees


def prune(tree):
    priority_queue = []
    priority_queue.append(tree)

    while len(priority_queue) > 0:

        current_node = priority_queue[0]
        chisquare_current = count_chisquare(current_node)
        chisquare_left = count_chisquare(current_node['left'])
        chisquare_right = count_chisquare(current_node['right'])
        if (chisquare_left > chisquare_current) or (chisquare_right > chisquare_current):
            if (current_node['left'] in priority_queue):
                priority_queue.remove(current_node['left'])
            if (current_node['right'] in priority_queue):
                priority_queue.remove(current_node['right'])
            current_node['left'] = None
            current_node['right'] = None
            current_node['IsLeafNode'] = True
        else:
            if (can_be_added_to_queue(current_node['left'])):
                priority_queue.append(current_node['left'])
            if (can_be_added_to_queue(current_node['right'])):
                priority_queue.append(current_node['right'])
        priority_queue.remove(priority_queue[0])



def count_chisquare(tree):
    num_of_parent_population = tree['Positive(1)'] + tree['Negative(0)']
    chance_positive = tree['Positive(1)'] / num_of_parent_population
    chance_negative = tree['Negative(0)'] / num_of_parent_population
    left_child = tree['left']
    right_child = tree['right']

    chisquare_left_positive = count_chisquare_util(left_child['Positive(1)'] + left_child['Negative(0)'],
                                                   chance_positive, left_child['Positive(1)'])
    chisquare_left_negative = count_chisquare_util(left_child['Positive(1)'] + left_child['Negative(0)'],
                                                   chance_negative, left_child['Negative(0)'])
    chisquare_right_positive = count_chisquare_util(right_child['Positive(1)'] + right_child['Negative(0)'],
                                                    chance_positive, right_child['Positive(1)'])
    chisquare_right_negative = count_chisquare_util(right_child['Positive(1)'] + right_child['Negative(0)'],
                                                    chance_negative, right_child['Negative(0)'])
    return chisquare_left_negative + chisquare_left_positive + chisquare_right_negative + chisquare_right_positive


def count_chisquare_util(total_population, chance, class_population):
    return (total_population * chance - class_population)**2/(total_population * chance)




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

    def find_best_split_of_all(self, x, y):
        column = None
        min_entropy = 1
        cutoff = None

        for i, c in enumerate(x.T):
            entropy, current_cutoff = self.find_best_split(c, y)
            if not entropy:
                return i, current_cutoff, entropy
            elif entropy <= min_entropy:
                min_entropy = entropy
                column = i
                cutoff = current_cutoff
        return column, cutoff, min_entropy

    def fit(self, feature_set, target_variable, parent_node={}, depth=0):
        if parent_node is None:
            return None
        elif len(target_variable) == 0:
            return None
        # elif self.all_same(target_variable):
        #     return {'val': target_variable[0]}
        elif depth >= self.max_depth:
            return None
        else:
            column, cutoff, entropy = self.find_best_split_of_all(feature_set, target_variable)
            y_left = target_variable[feature_set[:, column] < cutoff]
            y_right = target_variable[feature_set[:, column] >= cutoff]
            parent_node = {'col': self.dataset.feature_names[column],
                           'index_col': column,
                           'cutoff': cutoff,
                           'Positive(1)': list(target_variable).count(1),
                           'Negative(0)':list(target_variable).count(0),
                           'val': np.round(np.mean(target_variable)),
                           'left': self.fit(feature_set[feature_set[:, column] < cutoff], y_left, {}, depth+1),
                           'right': self.fit(feature_set[feature_set[:, column] >= cutoff], y_right, {}, depth+1)
                           }
            self.depth += 1
            self.trees = parent_node
            return parent_node

    def all_same(self, items):
        return all(x == items[0] for x in items)

    def predict(self, test_data):
        assert hasattr(self, 'trees'), "The tree needs to be trained first. Use fit() to train."

        results = np.array([0]*len(test_data))
        for i, row in enumerate(test_data):
            results[i] = self._get_prediction(row)
        return results


    def _get_prediction(self, row):
        current_layer = self.trees
        while current_layer and current_layer.get('cutoff'):
            if row[current_layer['index_col']] < current_layer['cutoff']:
                if current_layer['left']:
                    current_layer = current_layer['left']
                else:
                    break
            else:
                if current_layer['right']:
                    current_layer = current_layer['right']
                else:
                    break
        return current_layer.get('val')

    



