import csv
import random
import sys

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.io.json import json_normalize
from scipy.spatial import KDTree
from IPython.display import display
from sklearn.metrics import mean_absolute_error

# shakespeare_word_list.json wc comes out to 886311 so we need an appropriate recursion limit for it 
sys.setrecursionlimit(90000)

#performs KNN regression
class Regression(object):
	def __init__(self):
		self.k = 5
		self.metric = np.mean
		self.kdtree = None
		self.words = None
		self.instances = None

	def set_data(self, words, instances):
		"""
		Sets words and instances data
		:param words: pandas.Dataframe with words parameter
		:param instances: pandas.Series with instances of words 
		"""
		self.words = words
		self.instances = instances
		self.kdtree = KDTree(self.words)

	def regress(self, query_point):
		_, indexes = self.kdtree.query(query_point, self.k)
		instance = self.metric(self.instances.iloc[indexes])
		if np.isnan(instance):
			raise Exception('Unexpected result')
		else:
			return instance

# Create training data for KNN analysis
class RegressionTest(object):
	def __init__(self):
		self.words = None
		self.values = None

	def load_csv_file(self, csv_file, limit=None):
		pass

	def tests(self, folds):
		holdout = 1 / float(folds)
		errors = []
		for _ in range(folds):
			values_regress, values_actual = self.test_regression(holdout)
			errors.append(mean_absolute_error(values_actual, values_regress))
		return errors

	def test_regression(self, holdout):
		test_rows = random.sample(self.words.index.tolist(),
						int(round(len(self.words) * holdout)))
		train_rows = set(range(len(self.words))) - set(test_rows)
		df_test = self.words.ix[test_rows]
		df_train = self.words.drop(test_rows)

		train_values = self.values.ix[train_rows]
		regression = Regression()
		regression.set_data(words=df_train, values = train_values)

		values_regr = []
		values_actual = []

		for idx, row in df_gest.iterrows():
			values_regr.append(regression.regress(row))
			values_actual.append(self.values[idx])
		return values_regr, values_actual