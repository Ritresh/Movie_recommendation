from preprocess import preprocess
from utils import stem

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pickle


def train():

    new_df_copy = preprocess()

    new_df_copy['tags']=new_df_copy['tags'].apply(stem)

    cv = CountVectorizer(max_features=5000,stop_words='english')

    vector = cv.fit_transform(new_df_copy['tags']).toarray()

    similarity = cosine_similarity(vector)

    pickle.dump(new_df_copy,open('models/movies.pkl','wb'))
    pickle.dump(similarity,open('models/model.pkl','wb'))


if __name__ == "__main__":
    train()