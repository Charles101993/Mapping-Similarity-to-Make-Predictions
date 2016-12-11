import pandas as pd
import numpy as np
import model1_predict
import models
import model4

from ast import literal_eval
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation, metrics

def k_fold_val(feature_data, target_data, model=LinearRegression()):

	kfold = cross_validation.KFold(len(feature_data), n_folds=10, shuffle=True, random_state=0)

	rsquared, mean_abs_err, mean_squared_err = 0, 0, 0
	for train_indices, test_indices in kfold:
		
		train_x, train_y, test_x, test_y = None, None, None, None
		
		# k-1 training data
		
		# is dataframe or series
		if isinstance(feature_data, pd.DataFrame) or isinstance(feature_data, pd.Series):
			train_x = feature_data.iloc[train_indices]
			train_y = target_data.iloc[train_indices]

			# test data
			test_x = feature_data.iloc[test_indices]
			test_y = target_data.iloc[test_indices]
			
		# else np array	
		else:
			train_x = feature_data[train_indices]
			train_y = target_data[train_indices]

			# test data
			test_x = feature_data[test_indices]
			test_y = target_data[test_indices]

		model = model.fit(train_x, train_y)

		# estimate for measuring error
		estimates = model.predict(test_x)

		# add metrics to totals
		rsquared = rsquared + model.score(test_x, test_y)
		mean_abs_err = mean_abs_err + metrics.mean_absolute_error(test_y, estimates)
		mean_squared_err = mean_squared_err + metrics.mean_squared_error(test_y, estimates)

	# get averages
	rsquared = rsquared/10
	mean_abs_err = mean_abs_err/10
	mean_squared_err = mean_squared_err/10

	return rsquared, mean_abs_err, mean_squared_err

# table of critics, movies, scores
df = pd.read_csv("clean1.csv")[["Critic","Title","Critic Score"]]

# shared movies matrix
# note: list values are read back as strings!
# convert with ast.literal_eval()
df_shared_adj = pd.read_csv("shared_title_matrix.csv", index_col=0).applymap(literal_eval)
critics = list(df_shared_adj.columns)
critics.remove("Mike D'Angelo")

"""
full_map = {}
for critic1 in critics:

	shared = set()
	
	# skip self
	other_critics = list(critics)
	other_critics.remove(critic1)
	
	for critic2 in other_critics:
		shared = shared.union( set(df_shared_adj[critic1].loc[critic2]) )
	
	# skip if not 2 or more titles
	if len(shared) > 6:
		full_map[critic1] = list(shared)

# split titles to train on and titles to test on
train_map = {}
test_map = {}
for key, value in full_map.iteritems():	

	train_map[key] = value[:len(value)/2]
	test_map[key] = value[len(value)/2:]


# build training set
train_target = []
train_a = []
train_b = []
train_c = []
train_d = []
for critic, titles in train_map.iteritems():
	
	for title in titles:
	
		target = df[ (df["Critic"]==critic) & (df["Title"]==title) ].values[0][2]
		a = model1_predict.predict(critic, title)
		b = models.model2(critic, title)
		c = models.model3(critic, title)
		d = model4.get_metascore(title)
	
		train_target.append( target )
		train_a.append( a )
		train_b.append( b )
		train_c.append( c )
		train_d.append( d )
	
train_df = pd.DataFrame()
train_df['Model 1'] = pd.Series(train_a)
train_df['Model 2'] = pd.Series(train_b)
train_df['Model 3'] = pd.Series(train_c)
train_df['Model 4'] = pd.Series(train_d)
train_df['Target'] = pd.Series(train_target)

train_df.to_csv("train.csv")
"""
train_df = pd.read_csv("train.csv", index_col=0)

length = len(train_df)

#train_df["Combined"] = train_df["Model 1"] + train_df["Model 2"] + train_df["Model 3"] / 3

train_features = train_df[["Model 1", "Model 2", "Model 3", "Model 4"]]
#train_features = train_df[["Combined", "Model 4"]]
train_target = train_df["Target"]

lm = LinearRegression()
lm.fit(train_features, train_target)

"""
# build test set
test_target = []
test_a = []
test_b = []
test_c = []
test_d = []
for critic, titles in test_map.iteritems():
	
	for title in titles:
	
		target = df[ (df["Critic"]==critic) & (df["Title"]==title) ].values[0][2]
		a = model1_predict.predict(critic, title)
		b = models.model2(critic, title)
		c = models.model3(critic, title)
		d = model4.get_metascore(title)
	
		test_target.append( target )
		test_a.append( a )
		test_b.append( b )
		test_c.append( c )
		test_d.append( d )

test_df = pd.DataFrame()
test_df['Model 1'] = pd.Series(test_a)
test_df['Model 2'] = pd.Series(test_b)
test_df['Model 3'] = pd.Series(test_c)
test_df['Model 4'] = pd.Series(test_d)
test_df['Target'] = pd.Series(test_target)

test_df.to_csv("test.csv")
"""
test_df = pd.read_csv("test.csv", index_col=0)

length = len(test_df)

#test_df["Combined"] = test_df["Model 1"] + test_df["Model 2"] + test_df["Model 3"] / 3

test_features = test_df[["Model 1", "Model 2", "Model 3", "Model 4"]]
#test_features = test_df[["Combined", "Model 4"]]
test_target = test_df["Target"]


print "\nTraining Set Accuracy 50/50: ", lm.score(train_features, train_target)
print "\nTesting Set Accuracy 50/50: ", lm.score(test_features, test_target)

full_df = train_df.append(test_df)

full_features = full_df[["Model 1", "Model 2", "Model 3", "Model 4"]]
full_target = full_df["Target"]

print full_features.shape
print full_target.shape

print "\nFor K-Fold, \n\tR-Squared: %s\n\tMean Absolute Error: %s\n\tMean Squared Error: %s" % k_fold_val(full_features, full_target, LinearRegression())

		
