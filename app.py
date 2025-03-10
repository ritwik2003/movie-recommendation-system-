#api_key = 4150bd5ca9e960f527d69c5701045bc0
import streamlit as st
import pickle
import pandas as pd
import requests



movies_d = pickle.load(open('movies_d.pkl','rb'))
movies = pd.DataFrame(movies_d)

def get_poster(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4150bd5ca9e960f527d69c5701045bc0'.format(id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]



def recommend_movies(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_idx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend = []
    posters_p=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend.append(movies.iloc[i[0]].title)
        posters_p.append(get_poster(movie_id))
    return recommend,posters_p

st.title("Movie recommendation System")
select_movies = st.selectbox("Movies",movies["title"].values)
similarity = pickle.load(open('similarity.pkl','rb'))
if st.button("Recommend"):
    recommendations,posters = recommend_movies(select_movies)
    # for i in recommendations:
    #     st.write(i)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.write(recommendations[0])
        st.image(posters[0])

    with col2:
        st.write(recommendations[1])
        st.image(posters[1])

    with col3:
        st.write(recommendations[2])
        st.image(posters[2])

    with col4:
        st.write(recommendations[3])
        st.image(posters[3])

    with col5:
        st.write(recommendations[4])
        st.image(posters[4])


