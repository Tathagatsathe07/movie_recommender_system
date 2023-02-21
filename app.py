import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_posture(movie_id):
    respone = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b98fc9549f9a510dbd54105bf848c415&language=en-U'.format(movie_id))
    data = respone.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movies_id


        recommended_movie.append(movies.iloc[i[0]].title)
        # fetch posture from API
        recommended_movie_posters.append(fetch_posture(movie_id))
    return recommended_movie,recommended_movie_posters

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which Movie you want to Watch ?',
movies['title'].values)


if st.button('recommend'):
   names,posters =  recommend(selected_movie_name)

   col1,col2,col3,col4,col5=st.columns(5)
   with col1:
       st.text(names[0])
       st.image(posters[0])
   with col2:
       st.text(names[1])
       st.image(posters[1])
   with col3:
       st.text(names[2])
       st.image(posters[2])
   with col4:
       st.text(names[3])
       st.image(posters[3])
   with col5:
       st.text(names[4])
       st.image(posters[4])

























