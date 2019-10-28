"""Learning from examples. (Chapters 18)"""

import copy
import math
import random
from collections import defaultdict
from statistics import mean, stdev

from utils import mean_boolean_error, parse_csv, open_data, remove_all, unique, argmax_random_tie, normalize, \
    weighted_sample_with_replacement


class DataSet:
    """
    A data set for a machine learning problem. It has the following fields:

    d.examples   A list of examples. Each one is a list of attribute values.
    d.attrs      A list of integers to index into an example, so example[attr]
                 gives a value. Normally the same as range(len(d.examples[0])).
    d.attr_names Optional list of mnemonic names for corresponding attrs.
    d.target     The attribute that a learning algorithm will try to predict.
                 By default the final attribute.
    d.inputs     The list of attrs without the target.
    d.values     A list of lists: each sublist is the set of possible
                 values for the corresponding attribute. If initially None,
                 it is computed from the known examples by self.set_problem.
                 If not None, an erroneous value raises ValueError.
    d.distance   A function from a pair of examples to a non-negative number.
                 Should be symmetric, etc. Defaults to mean_boolean_error
                 since that can handle any field types.
    d.name       Name of the data set (for output display only).
    d.source     URL or other source where the data came from.
    d.exclude    A list of attribute indexes to exclude from d.inputs. Elements
                 of this list can either be integers (attrs) or attr_names.

    Normally, you call the constructor and you're done; then you just
    access fields like d.examples and d.target and d.inputs.
    """

    def __init__(self, examples=None, attrs=None, attr_names=None, target=-1, inputs=None,
                 values=None, distance=mean_boolean_error, name='', source='', exclude=()):
        """
        Accepts any of DataSet's fields. Examples can also be a
        string or file from which to parse examples using parse_csv.
        Optional parameter: exclude, as documented in .set_problem().
        >>> DataSet(examples='1, 2, 3')
        <DataSet(): 1 examples, 3 attributes>
        """
        self.name = name
        self.source = source
        self.values = values
        self.distance = distance
        self.got_values_flag = bool(values)

        # initialize .examples from string or list or data directory
        if isinstance(examples, str):
            self.examples = parse_csv(examples)
        elif examples is None:
            self.examples = parse_csv(open_data(name + '.csv').read())
        else:
            self.examples = examples

        # attrs are the indices of examples, unless otherwise stated.
        if self.examples is not None and attrs is None:
            attrs = list(range(len(self.examples[0])))

        self.attrs = attrs

        # initialize .attr_names from string, list, or by default
        if isinstance(attr_names, str):
            self.attr_names = attr_names.split()
        else:
            self.attr_names = attr_names or attrs
        self.set_problem(target, inputs=inputs, exclude=exclude)

    def set_problem(self, target, inputs=None, exclude=()):
        """
        Set (or change) the target and/or inputs.
        This way, one DataSet can be used multiple ways. inputs, if specified,
        is a list of attributes, or specify exclude as a list of attributes
        to not use in inputs. Attributes can be -n .. n, or an attr_name.
        Also computes the list of possible values, if that wasn't done yet.
        """
        self.target = self.attr_num(target)
        exclude = list(map(self.attr_num, exclude))
        if inputs:
            self.inputs = remove_all(self.target, inputs)
        else:
            self.inputs = [a for a in self.attrs if a != self.target and a not in exclude]
        if not self.values:
            self.update_values()
        self.check_me()

    def check_me(self):
        """Check that my fields make sense."""
        assert len(self.attr_names) == len(self.attrs)
        assert self.target in self.attrs
        assert self.target not in self.inputs
        assert set(self.inputs).issubset(set(self.attrs))
        if self.got_values_flag:
            # only check if values are provided while initializing DataSet
            list(map(self.check_example, self.examples))

    def add_example(self, example):
        """Add an example to the list of examples, checking it first."""
        self.check_example(example)
        self.examples.append(example)

    def check_example(self, example):
        """Raise ValueError if example has any invalid values."""
        if self.values:
            for a in self.attrs:
                if example[a] not in self.values[a]:
                    raise ValueError('Bad value {} for attribute {} in {}'
                                     .format(example[a], self.attr_names[a], example))

    def attr_num(self, attr):
        """Returns the number used for attr, which can be a name, or -n .. n-1."""
        if isinstance(attr, str):
            return self.attr_names.index(attr)
        elif attr < 0:
            return len(self.attrs) + attr
        else:
            return attr

    def update_values(self):
        self.values = list(map(unique, zip(*self.examples)))

    def sanitize(self, example):
        """Return a copy of example, with non-input attributes replaced by None."""
        return [attr_i if i in self.inputs else None for i, attr_i in enumerate(example)]

    def classes_to_numbers(self, classes=None):
        """Converts class names to numbers."""
        if not classes:
            # if classes were not given, extract them from values
            classes = sorted(self.values[self.target])
        for item in self.examples:
            item[self.target] = classes.index(item[self.target])

    def remove_examples(self, value=''):
        """Remove examples that contain given value."""
        self.examples = [x for x in self.examples if value not in x]
        self.update_values()

    def split_values_by_classes(self):
        """Split values into buckets according to their class."""
        buckets = defaultdict(lambda: [])
        target_names = self.values[self.target]

        for v in self.examples:
            item = [a for a in v if a not in target_names]  # remove target from item
            buckets[v[self.target]].append(item)  # add item to bucket of its class

        return buckets

    def find_means_and_deviations(self):
        """
        Finds the means and standard deviations of self.dataset.
        means     : a dictionary for each class/target. Holds a list of the means
                    of the features for the class.
        deviations: a dictionary for each class/target. Holds a list of the sample
                    standard deviations of the features for the class.
        """
        target_names = self.values[self.target]
        feature_numbers = len(self.inputs)

        item_buckets = self.split_values_by_classes()

        means = defaultdict(lambda: [0] * feature_numbers)
        deviations = defaultdict(lambda: [0] * feature_numbers)

        for t in target_names:
            # find all the item feature values for item in class t
            features = [[] for _ in range(feature_numbers)]
            for item in item_buckets[t]:
                for i in range(feature_numbers):
                    features[i].append(item[i])

            # calculate means and deviations fo the class
            for i in range(feature_numbers):
                means[t][i] = mean(features[i])
                deviations[t][i] = stdev(features[i])

        return means, deviations

    def __repr__(self):
        return '<DataSet({}): {:d} examples, {:d} attributes>'.format(self.name, len(self.examples), len(self.attrs))


def err_ratio(predict, dataset, examples=None, verbose=0):
    """
    Return the proportion of the examples that are NOT correctly predicted.
    verbose - 0: No output; 1: Output wrong; 2 (or greater): Output correct
    """
    examples = examples or dataset.examples
    if len(examples) == 0:
        return 0.0
    right = 0
    for example in examples:
        desired = example[dataset.target]
        output = predict(dataset.sanitize(example))
        if output == desired:
            right += 1
            if verbose >= 2:
                print('   OK: got {} for {}'.format(desired, example))
        elif verbose:
            print('WRONG: got {}, expected {} for {}'.format(output, desired, example))
    return 1 - (right / len(examples))


def grade_learner(predict, tests):
    """
    Grades the given learner based on how many tests it passes.
    tests is a list with each element in the form: (values, output).
    """
    return mean(int(predict(X) == y) for X, y in tests)


def train_test_split(dataset, start=None, end=None, test_split=None):
    """
    If you are giving 'start' and 'end' as parameters,
    then it will return the testing set from index 'start' to 'end'
    and the rest for training.
    If you give 'test_split' as a parameter then it will return
    test_split * 100% as the testing set and the rest as
    training set.
    """
    examples = dataset.examples
    if test_split is None:
        train = examples[:start] + examples[end:]
        val = examples[start:end]
    else:
        total_size = len(examples)
        val_size = int(total_size * test_split)
        train_size = total_size - val_size
        train = examples[:train_size]
        val = examples[train_size:total_size]

    return train, val


class DecisionFork:
    """
    A fork of a decision tree holds an attribute to test, and a dict
    of branches, one for each of the attribute's values.
    """

    def __init__(self, attr, attr_name=None, default_child=None, branches=None):
        """Initialize by saying what attribute this node tests."""
        self.attr = attr
        self.attr_name = attr_name or attr
        self.default_child = default_child
        self.branches = branches or {}

    def __call__(self, example):
        """Given an example, classify it using the attribute and the branches."""
        attr_val = example[self.attr]
        if attr_val in self.branches:
            return self.branches[attr_val](example)
        else:
            # return default class when attribute is unknown
            return self.default_child(example)

    def add(self, val, subtree):
        """Add a branch.  If self.attr = val, go to the given subtree."""
        self.branches[val] = subtree

    def display(self, indent=0):
        name = self.attr_name
        print('Test', name)
        for (val, subtree) in self.branches.items():
            print(' ' * 4 * indent, name, '=', val, '==>', end=' ')
            subtree.display(indent + 1)

    def __repr__(self):
        return 'DecisionFork({0!r}, {1!r}, {2!r})'.format(self.attr, self.attr_name, self.branches)


class DecisionLeaf:
    """A leaf of a decision tree holds just a result."""

    def __init__(self, result):
        self.result = result

    def __call__(self, example):
        return self.result

    def display(self):
        print('RESULT =', self.result)

    def __repr__(self):
        return repr(self.result)


def DecisionTreeLearner(dataset):
    """[Figure 18.5]"""

    target, values = dataset.target, dataset.values

    def decision_tree_learning(examples, attrs, parent_examples=()):
        if len(examples) == 0:
            return plurality_value(parent_examples)
        if all_same_class(examples):
            return DecisionLeaf(examples[0][target])
        if len(attrs) == 0:
            return plurality_value(examples)
        A = choose_attribute(attrs, examples)
        tree = DecisionFork(A, dataset.attr_names[A], plurality_value(examples))
        for (v_k, exs) in split_by(A, examples):
            subtree = decision_tree_learning(exs, remove_all(A, attrs), examples)
            tree.add(v_k, subtree)
        return tree

    def plurality_value(examples):
        """
        Return the most popular target value for this set of examples.
        (If target is binary, this is the majority; otherwise plurality).
        """
        popular = argmax_random_tie(values[target], key=lambda v: count(target, v, examples))
        return DecisionLeaf(popular)

    def count(attr, val, examples):
        """Count the number of examples that have example[attr] = val."""
        return sum(e[attr] == val for e in examples)

    def all_same_class(examples):
        """Are all these examples in the same target class?"""
        class0 = examples[0][target]
        return all(e[target] == class0 for e in examples)

    def choose_attribute(attrs, examples):
        """Choose the attribute with the highest information gain."""
        return argmax_random_tie(attrs, key=lambda a: information_gain(a, examples))

    def information_gain(attr, examples):
        """Return the expected reduction in entropy from splitting by attr."""

        def I(examples):
            return information_content([count(target, v, examples) for v in values[target]])

        N = len(examples)
        remainder = sum((len(examples_i) / N) * I(examples_i) for (v, examples_i) in split_by(attr, examples))
        return I(examples) - remainder

    def split_by(attr, examples):
        """Return a list of (val, examples) pairs for each val of attr."""
        return [(v, [e for e in examples if e[attr] == v]) for v in values[attr]]

    return decision_tree_learning(dataset.examples, dataset.inputs)


def information_content(values):
    """Number of bits to represent the probability distribution in values."""
    probabilities = normalize(remove_all(0, values))
    return sum(-p * math.log2(p) for p in probabilities)


def replicated_dataset(dataset, weights, n=None):
    """Copy dataset, replicating each example in proportion to its weight."""
    n = n or len(dataset.examples)
    result = copy.copy(dataset)
    result.examples = weighted_replicate(dataset.examples, weights, n)
    return result


def weighted_replicate(seq, weights, n):
    """
    Return n selections from seq, with the count of each element of
    seq proportional to the corresponding weight (filling in fractions
    randomly).
    >>> weighted_replicate('ABC', [1, 2, 1], 4)
    ['A', 'B', 'B', 'C']
    """
    assert len(seq) == len(weights)
    weights = normalize(weights)
    wholes = [int(w * n) for w in weights]
    fractions = [(w * n) % 1 for w in weights]
    return (flatten([x] * nx for x, nx in zip(seq, wholes)) +
            weighted_sample_with_replacement(n - sum(wholes), seq, fractions))


def flatten(seqs):
    return sum(seqs, [])


def Majority(k, n):
    """
    Return a DataSet with n k-bit examples of the majority problem:
    k random bits followed by a 1 if more than half the bits are 1, else 0.
    """
    examples = []
    for i in range(n):
        bits = [random.choice([0, 1]) for _ in range(k)]
        bits.append(int(sum(bits) > k / 2))
        examples.append(bits)
    return DataSet(name='majority', examples=examples)


def Parity(k, n, name='parity'):
    """
    Return a DataSet with n k-bit examples of the parity problem:
    k random bits followed by a 1 if an odd number of bits are 1, else 0.
    """
    examples = []
    for i in range(n):
        bits = [random.choice([0, 1]) for _ in range(k)]
        bits.append(sum(bits) % 2)
        examples.append(bits)
    return DataSet(name=name, examples=examples)


def Xor(n):
    """Return a DataSet with n examples of 2-input xor."""
    return Parity(2, n, name='xor')


def ContinuousXor(n):
    """2 inputs are chosen uniformly from (0.0 .. 2.0]; output is xor of ints."""
    examples = []
    for i in range(n):
        x, y = [random.uniform(0.0, 2.0) for _ in '12']
        examples.append([x, y, x != y])
    return DataSet(name='continuous xor', examples=examples)
