import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pickle
from src.predict import recommend

new_df_copy = pickle.load(open('models/movies.pkl','rb'))

st.title("Movie Recommender System")

movie_list = new_df_copy['title'].values

selected_movie = st.selectbox("Select movie", movie_list)

if st.button("Recommend"):

    result = recommend(selected_movie)

    for i in result:
        st.write(i)
