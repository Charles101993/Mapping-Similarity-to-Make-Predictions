import pandas as pd
import numpy as np

# table of critics, movies, scores
df = pd.read_csv("clean1.csv")[["Title","Metascore"]].drop_duplicates("Title")

def get_metascore(title):
	
	score = df[ df["Title"]==title ]["Metascore"].values[0]
	if score == "tbd":
		return 60
	else: return int(score)
	
if __name__ == "__main__":
	
	print get_metascore("Looper")