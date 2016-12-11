import pandas as pd

file_name  = 'clean_charles.csv'
clean_csv = pd.read_csv(file_name, header = None)
clean_csv.columns = ['Critic', 'movie', 'm_score', 'c_score','review_text']
adj_df = pd.read_csv('clean_matrix_2.csv', header = 0, index_col = 0)
model_3_df = pd.read_csv('clean_matrix_3.csv', header = 0, index_col = 0)
def model3(movie_r , movie_):
    movie_reviewer = movie_r
    movie = movie_
    movie_df = clean_csv.loc[(clean_csv['movie'] == movie)]
    
    if len(movie_df) == 0:
	return 50
	
    p1 = 0.0
    p2 = 0.0
    p3 = 0.0
    p1_n = ''
    p2_n = ''
    p3_n = ''
    
    for i in movie_df['Critic']:
        temp = model_3_df.get_value(i, movie_reviewer)
        if p1 < temp:
            p3 = p2
            p3_n = p2_n
            p2 = p1
            p2_n = p1_n
            p1 = temp
            p1_n = i
        elif p2 < temp:
            p3 = p2
            p3_n = p2_n
            p2 = temp
            p2_n = i
        elif p3 < temp:
            p3 = temp
            p3_n = i

    #print movie_df
    index_ = movie_df[movie_df['Critic'] == p1_n].index.tolist()
    p1_v = movie_df.get_value(index_[0], 'c_score')
    index_ = movie_df[movie_df['Critic'] == p2_n].index.tolist()
    p2_v = movie_df.get_value(index_[0], 'c_score')
    # index_ = movie_df[movie_df['Critic'] == p3_n].index.tolist()
    # p3_v = movie_df.get_value(index_[0], 'c_score')


    prediction_val = (p1_v)

    if (p1_n == movie_reviewer):
        prediction_val = p2_v

    return prediction_val

#print model_3_df



#print new_list
def model2(movie_r , movie_):
    movie_reviewer = movie_r
    movie = movie_
    #adj_df.index = new_new['Critic'].unique()

    movie_df = clean_csv.loc[(clean_csv['movie'] == movie)]
    
    if len(movie_df) == 0:
	return 50

    p1 = 0.0
    p2 = 0.0
    p3 = 0.0
    p1_n = ''
    p2_n = ''
    p3_n = ''
    
    for i in movie_df['Critic']:
        temp = adj_df.get_value(i, movie_reviewer)
        if p1 < temp:
            p3 = p2
            p3_n = p2_n
            p2 = p1
            p2_n = p1_n
            p1 = temp
            p1_n = i
        elif p2 < temp:
            p3 = p2
            p3_n = p2_n
            p2 = temp
            p2_n = i
        elif p3 < temp:
            p3 = temp
            p3_n = i
	     
    #print movie_df
    index_ = movie_df[movie_df['Critic'] == p1_n].index.tolist()
    p1_v = movie_df.get_value(index_[0], 'c_score')
    # index_ = movie_df[movie_df['Critic'] == p2_n].index.tolist()
    # p2_v = movie_df.get_value(index_[0], 'c_score')
    # index_ = movie_df[movie_df['Critic'] == p3_n].index.tolist()
    # p3_v = movie_df.get_value(index_[0], 'c_score')

    prediction_val = (p1_v)

    return prediction_val