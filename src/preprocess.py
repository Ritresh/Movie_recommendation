import numpy as np
import pandas as pd
import ast

def preprocess():

    df_movies = pd.read_csv('data/raw/tmdb_5000_movies.csv')
    df_credits = pd.read_csv('data/raw/tmdb_5000_credits.csv')

    df_merge=df_movies.merge(df_credits,on='title')

    df_copy = df_merge.copy(deep=True)

    df_copy=df_copy[['movie_id','title','overview','genres','keywords','cast','crew']]

    df_copy.dropna(inplace=True)


    def convert(obj):
        if isinstance(obj, str):
            hai= [i['name'] for i in ast.literal_eval(obj)]
            return hai
        elif isinstance(obj, list):
            return obj
        else:
            return []


    df_copy['genres'] = df_copy['genres'].apply(convert)
    df_copy['keywords'] = df_copy['keywords'].apply(convert)


    def convert3(obj):
        L = []
        counter = 0

        if isinstance(obj, str):
            lis = ast.literal_eval(obj)

        for i in lis:
            if counter < 3:
                if isinstance(i, dict):
                    L.append(i['name'])
                else:
                    L.append(i)
                counter += 1
            else:
                break

        return L


    df_copy['cast']=df_copy['cast'].apply(convert3)


    def director(obj):
        L=[]
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                L.append(i['name'])
                break
        return L  


    df_copy['crew'] = df_copy['crew'].apply(director)

    df_copy['overview'] = df_copy['overview'].apply(lambda x:x.split())


    for col in ['crew','genres','keywords','cast']:
        df_copy[col] = df_copy[col].apply(lambda x: [i.replace(" ","") for i in x] if isinstance(x, list) else [])


    df_copy['tags'] =  df_copy['overview']+ df_copy['genres']+ df_copy['keywords']+ df_copy['cast']+ df_copy['crew']

    new_df_copy = df_copy[['movie_id','title','tags']]

    new_df_copy['tags'] = new_df_copy['tags'].apply(lambda x:' '.join(x))

    new_df_copy['tags'] = new_df_copy['tags'].apply(lambda x:x.lower())

    return new_df_copy