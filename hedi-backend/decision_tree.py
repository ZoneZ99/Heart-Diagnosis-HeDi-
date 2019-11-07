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

	def all_same(self, items):
		return all(x == items[0] for x in items)

	def fit(self, feature_set, target_variable, parent_node={}, depth=0):
		if parent_node is None:
			return None
		elif len(target_variable) == 0:
			return None
		elif self.all_same(target_variable):
			return {'val': target_variable[0]}
		elif depth >= self.max_depth:
			return None
		else:
			column, cutoff, entropy = self.find_best_split_of_all(feature_set, target_variable)
			y_left = target_variable[feature_set[:, column] < cutoff]
			y_right = target_variable[feature_set[:, column] >= cutoff]
			parent_node = {'col': self.dataset.feature_names[column],
						   'index_col': column,
						   'cutoff': cutoff,
						   'val': np.round(np.mean(target_variable)),
						   'left': self.fit(feature_set[feature_set[:, column] < cutoff], y_left, {}, depth+1),
						   'right': self.fit(feature_set[feature_set[:, column] >= cutoff], y_right, {}, depth+1)
						   }
			self.depth += 1
			self.trees = parent_node
			return parent_node
