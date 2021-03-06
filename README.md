#Similarity Matrix for Movie Reviewers 

##Team members:
Charles Beehner  
Dan Banks


##Overview

[Google Drive](https://drive.google.com/drive/folders/0B_2e_AVgx5V6WVljNjRpdWhmUVk?usp=sharing)      
[Notebook](https://github.tamu.edu/pages/danbanks15/Mapping-Similarity-to-Make-Predictions/Mapping%20Similarity%20to%20Make%20Predictions.html)    
[Video](https://www.youtube.com/watch?v=rmDODFpM6Js)    
[Webpage](https://github.tamu.edu/pages/danbanks15/Mapping-Similarity-to-Make-Predictions/)   

We wanted to create a way to group people based on similarities between them, then use those similarities to make predictions about a particular persons behavior.
To test the predictive validity of our approach we gathered data on movie critics from metacritic. Using their scores and reviews we constructed 3 different models of similarity. We combined those 3 models into a single model and queried it using a movie and a movie critic to get the predicted critic score from our model. We then checked it against the actual score of the movie critic to get a sense of how accurate similarity scalers were at prediciting the score of the movie critic we cared about.

##Implications
It is not much of a secret that people are impressionable. As we grow older everything from our taste in music, religion, food, politics, etc. is conditioned directly or indirectly from the people we interact with. Therefore, it seems reasonable that if two people are similar and one of those people exhibits some measurable behavior, then the other person will probably exhibit a similar behavior when in the same context. If this turns out to be true, we could not only make better movie reccomendations to people, but also we could also categorize the tasters and the tastemakers into smaller and smaller groups and target local to popularize a new product or service. Moreover, we could identify tendencies in behaviors of musicians, artists, researchers, chefs, and movie makers to figure out which ones are derivative and which ones are inventive. Say for instance you're into the most obscure and underground music on the planet, and you want to know if your favorite band really is the most perplexing and misunderstood archimedian transcedent geniouses they claim to be. You could use our model to plot an adjecency matrix against other musicians (using features like lyrics, notes, transcripts of band interviews, etc.) to verify this fact.

##Proceedure
We collected data about critics from MetaCritic. The data collected includes:   
    1. The name of the movie critic   
    2. The movies reviewed by the critic    
    3. The review text of the critic for a particular movie   
    4. The score of the movie given by the critic   
    5. The MetaCritic score for the movie
Our final, cleaned dataset contained 189 critics with about 55,000 reviews (and scores) in total.

Once this was done we created 3 adjecency matrices. 
The first, gave us similarity scalars of scores different critics gave the same movie. 
The second, gave us similarity scores based on the synonymic similarity of the language used in their reviews to the language other reviewers used in there reviews.
We used wordnet to evaluate words in each critics review, and compared it to the words in the reviews of other critics, we used found the "path_similarity" which was a floating point value between 0 and 1. We added these values to construct the second similarity matrix.
And the third gave us a similarity scalar matrix of the instances of words used in different reviews by different critics. All of these matrices made it possible for use to take in a movie and critic name and output the most similar critic based on the features in each model. Then the output would be a weighted mean of the critics which were similar to the critic you wanted to know about.

#Take aways
Through some trial and error we were able to improve our model's accuracy, although the final model is still not strong enough to make good predictions. What we noticed is that adding more observation features produced the most significant results and that refinement through manipulation of existing features was not as powerful as we had anticipated. We believe our focus on the perplexity of our model hindered its potential. In the future, more raw variables should be collected and analysed. Also, the computation and memory involved in manipulating features made it almost intractable to do reasonable sentiment analysis over all of our review text. Despite our failure to make good predictions, we are extremely optimistic about the viability of this approach. It is our opinion that mapping similarities between groups of people should have tremendous potential for predicting uncertain human behaviors.
