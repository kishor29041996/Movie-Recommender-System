try:
    import streamlit as st
except ModuleNotFoundError:
    raise ImportError("streamlit is required. Install it with `pip install streamlit`") from None
import pandas as pd
import pickle

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommender System")
st.write("Select a movie and get 4 similar movie recommendations.")

# ----------------------------
# LOAD DATA
# ----------------------------
# movies.pkl should contain a dataframe with:
# columns -> movie_id, title
#
# similarity.pkl should contain similarity matrix

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies['title'].values


# ----------------------------
# RECOMMEND FUNCTION
# ----------------------------
def recommend(movie):
    
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    # sort based on similarity score
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:5]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies


# ----------------------------
# UI
# ----------------------------
selected_movie = st.selectbox(
    "Choose a movie",
    movie_list
)

if st.button("Recommend"):
    
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    col1, col2 = st.columns(2)

    with col1:
        st.success(recommendations[0])
        st.success(recommendations[1])

    with col2:
        st.success(recommendations[2])
        st.success(recommendations[3])