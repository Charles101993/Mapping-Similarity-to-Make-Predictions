import pandas as pd
import numpy as np

df = pd.read_csv("clean1.csv")[["Critic","Title"]]

critics_list = df["Critic"].drop_duplicates().values

shared_matrix = pd.DataFrame(columns=critics_list, index=critics_list)

for i, critic1 in enumerate(critics_list):

	critic1_titles = df[ df["Critic"]==critic1 ]
	
	#print "\n" + critic1 + " - seen movies: " + str(len(critic1_titles))
	
	shared_titles_list = []
	
	# use adjacency matrix to get title intersections calculated before 
	for critic2 in critics_list[:i]:

		shared_titles_list.append( list(shared_matrix.loc[critic2][critic1]) )
	
	# for diagonal cell
	shared_titles_list.append( df[ df["Critic"]==critic1 ]["Title"].values.tolist() )
	
	# get values by calculating
	for critic2 in critics_list[i+1:]:

		critic2_titles = df[ df["Critic"]==critic2 ]
			
		shared_titles = set(critic1_titles["Title"].values).intersection(set(critic2_titles["Title"].values))		
		
		shared_titles_list.append(list(shared_titles))

	shared_matrix.loc[critic1] = shared_titles_list

shared_matrix.to_csv("shared_title_matrix.csv")