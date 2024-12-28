
import streamlit as st
import requests
import pickle
import pandas as pd
from joblib import load
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# YouTube API key
API_KEY = os.getenv("MY_API")

# Base URL for YouTube API
API_URL = 'https://www.googleapis.com/youtube/v3/search'

# Function to fetch videos from YouTube
def fetch_videos(query, max_results=1):
    url = f'{API_URL}?part=snippet&maxResults={max_results}&q={query}+trailer&type=video&key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['items']
    else:
        st.error("Error fetching videos.")
        return []


# Function for anime recommendations
def recommend(anime, animeList, similarity):
    anime_index = animeList[animeList['English name'] == anime].index[0]
    distances = similarity[anime_index]
    ani_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:25]

    recommended_anime_images = []
    recommended_anime_names = []
    for i in ani_list:
        recommended_anime_images.append(animeList.iloc[i[0]]['Image URL'])
        recommended_anime_names.append(animeList.iloc[i[0]]['English name'])

    return recommended_anime_names, recommended_anime_images


# Load anime data and similarity matrix
anime_dict = pickle.load(open('anime_dict.pkl', 'rb'))
animeList = pd.DataFrame(anime_dict)
similarity = load('similarities.pkl')


# Define the Anime Recommendations Page
def anime_recommendations_page():
    st.title('Anime Recommender System')

    # Select an anime for recommendations
    selected_anime_name = st.selectbox('Select the Anime', animeList['English name'].values)

    if selected_anime_name:
        # Fetch recommendations for the selected anime
        names, images = recommend(selected_anime_name, animeList, similarity)

        # Display recommendations with thumbnails
        st.subheader(f"Recommendations for {selected_anime_name}")
        cols = st.columns(3)  # Display 3 recommendations per row
        buttons = []  # To store which button was clicked

        for i in range(0, len(names), 3):
            row_names = names[i:i + 3]
            row_images = images[i:i + 3]

            # Loop through the columns in the row
            for col, name, image in zip(cols, row_names, row_images):
                with col:
                    st.image(image, width=250)  # Set width for consistency
                    st.markdown(f"**{name}**")
                    # Display buttons for each recommendation
                    if st.button(f"Watch Trailer", key=image):
                        buttons.append(name)

        if buttons:
            # Redirect to the trailer page for the clicked anime
            st.session_state.clicked_anime = buttons[-1]
            st.write("Redirecting to trailer page...")
            st.switch_page(st.Page(trailer_page,title='Watch Trailer',icon="🎥"))


def trailer_page():
    st.title('Trailer Viewer')

    clicked_anime = st.session_state.get('clicked_anime', None)

    if clicked_anime:
        st.subheader(f"Trailer of {clicked_anime}")

        # Fetch YouTube trailer for the selected anime
        videos = fetch_videos('Trailer for '+clicked_anime+' anime')
        if videos:
            video_id = videos[0]['id']['videoId']
            st.video(f'https://www.youtube.com/watch?v={video_id}')
        else:
            st.error("Trailer not found.")
    else:
        st.error("No anime selected for trailer.")


# Set up Streamlit navigation
pg = st.navigation([
    st.Page(anime_recommendations_page, title="Anime Recommendations", icon="🔥"),
    st.Page(trailer_page, title="Watch Trailer", icon="🎥")
])

# Run the selected page
pg.run()
