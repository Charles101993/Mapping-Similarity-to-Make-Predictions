import pandas as pd
import numpy as np

from ast import literal_eval

# table of critics, movies, scores
df = pd.read_csv("clean1.csv")[["Critic","Title","Critic Score"]]

# relationship matrix
df_score_adj = pd.read_csv("critic_score_rel_matrix3.csv", index_col=0)

# difference matrix
df_diff_adj = pd.read_csv("critic_score_diff_matrix.csv", index_col=0)

# shared movies matrix
# note: list values are read back as strings!
# convert with ast.literal_eval()
df_shared_adj = pd.read_csv("shared_title_matrix.csv", index_col=0).applymap(literal_eval)

def predict(critic, title):
	
	# get score if already exists for critic
	# score = df[ (df["Critic"]==critic) & (df["Title"]==title) ]
	# if len(score) != 0:
		# return score.values[0]
		
	ordered_critics = list(df_score_adj[critic].sort_values(ascending=False).index)
	ordered_critics.remove(critic)
	
	total_critics = 0
	score_list = []
	for critic2 in ordered_critics:
	
		if total_critics == 3: break
		
		shared = df_shared_adj[critic].loc[critic2]
			
		for string in shared:
			if string == title:
				total_critics+=1
				score_list.append( df[ (df["Critic"]==critic2) & (df["Title"]==title) ].values[0][2] + df_diff_adj[critic].loc[critic2] )
	
	if total_critics == 1:
		return score_list[0]
	if total_critics == 2:
		weights = [0.7,0.3]
		return sum([a*b for a,b in zip(score_list,weights)])
	if total_critics == 3:
		weights = [0.7,0.2,0.1]
		return sum([a*b for a,b in zip(score_list,weights)])
	else:
		return "No one has seen it!"
	
if __name__ == "__main__":
	
	print predict("Peter Travers","Looper")
	print df[ (df["Critic"]=="Peter Travers") & (df["Title"]=="Looper") ].values[0][2]	