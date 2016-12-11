import pandas as pd
import numpy as np
import math

df = pd.read_csv("clean1.csv")[["Critic","Title","Critic Score"]]

critics_list = df["Critic"].drop_duplicates().values

relationship_matrix = pd.DataFrame(columns=critics_list, index=critics_list)

for i, critic1 in enumerate(critics_list):

	critic1_scores = df[ df["Critic"]==critic1 ]	
	critic1_titles = critic1_scores["Title"].values
	
	similarity_ratios = []
	for critic2 in critics_list:
		
		if critic1 == critic2:
			similarity_ratios.append(100)
			continue
		
		critic2_scores = df[ df["Critic"]==critic2 ]
		critic2_titles = critic2_scores["Title"].values
		
		shared_titles = set(critic1_titles).intersection(set(critic2_titles))
		# add placeholder if no shared movies
		if not len(shared_titles):
			similarity_ratios.append(None)
			continue
		
		critic1_scores_temp = critic1_scores[ critic1_scores["Title"].isin(shared_titles) ].sort_values(by="Title").reset_index(drop=True)
		critic2_scores = critic2_scores[ critic2_scores["Title"].isin(shared_titles) ].sort_values(by="Title").reset_index(drop=True)
		
		# make sure we only consider movies with a critic score
		numeric_scores = critic1_scores_temp["Critic Score"].map(np.isreal) & critic2_scores["Critic Score"].map(np.isreal)

		critic1_scores_temp = critic1_scores_temp[ numeric_scores ].reset_index(drop=True)
		critic2_scores = critic2_scores[ numeric_scores ].reset_index(drop=True)
		
		differences = critic1_scores_temp["Critic Score"] - critic2_scores["Critic Score"]
		differences = differences.apply(abs)
		mean = differences.mean()
		
		n_shared = len(shared_titles)
		if n_shared >= 30: n_shared = 30
		
		# log(1)/log(30) = 0 <= confidence_index <= 1 = log( min(n_shared,30) )/log(30)
		confidence_index = math.log(n_shared)/math.log(30)
		mean_difference = 100 - mean
		similarity_ratios.append(mean_difference * confidence_index)

	relationship_matrix.loc[critic1] = similarity_ratios
	
relationship_matrix.to_csv("critic_score_rel_matrix3.csv")