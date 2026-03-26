import pickle

new_df_copy = pickle.load(open('models/movies.pkl','rb'))
similarity = pickle.load(open('models/model.pkl','rb'))


def recommend(movie):

    movie_index=new_df_copy[new_df_copy['title']==movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x:x[1]
    )[1:6]

    result=[]

    for i in movies_list:
        result.append(new_df_copy.iloc[i[0]].title)

    return result