# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:51:18 2023

@author: User
"""


import pandas as pd
import streamlit as st
import pickle 
import requests
from PIL import Image
import base64

movies_dict=pickle.load(open ('movies with posters.pkl','rb'))
movies_list=pd.DataFrame(movies_dict)
movies=movies_list['title'].values


similarity=pickle.load(open('similarity.pkl','rb'))




    

def recommend(movie):
    movie_index=movies_list[movies_list['title']==movie].index[0]
    distance=similarity[movie_index] 
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
     
    
    recommended_movies=[]
    recommended_movies_poster=[]
    
    for i in movie_list:
        
       
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_poster.append(movies_list.iloc[i[0]].poster_path)
        
    return   recommended_movies,recommended_movies_poster


import streamlit as st

st.markdown(
    f"""
    <h1 style='text-align: center; color: blue;'>Movie Recommendation system</h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wirally.com/wp-content/uploads/2016/10/tollywood1.jpg");
             background-attachment: fixed;
             background-size: cover
            
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

selected_movie=st.selectbox('Movie', (movies))
        

if st.button('recommend'):
    
    
    recommended_movies,recommended_movies_poster=recommend(selected_movie)
    
    col1, col2, col3 ,col4,col5= st.columns(5)

    with col1:
       st.text(recommended_movies[0])
       st.image("https://image.tmdb.org/t/p/w500"+recommended_movies_poster[0])

    with col2:
       st.text(recommended_movies[1])
       st.image("https://image.tmdb.org/t/p/w500"+recommended_movies_poster[1])
    with col3:
       st.text(recommended_movies[2])
       st.image("https://image.tmdb.org/t/p/w500"+recommended_movies_poster[2])

    with col4:
       st.text(recommended_movies[3])
       st.image("https://image.tmdb.org/t/p/w500"+recommended_movies_poster[3])

    with col5:
       st.text(recommended_movies[4])
       st.image("https://image.tmdb.org/t/p/w500"+recommended_movies_poster[4])