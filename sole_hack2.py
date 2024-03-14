import streamlit as st
import pandas as pd
import requests

# Chargement des données
url = 'https://github.com/sole-tolo/Hackathon_Two/blob/main/data_hack2.csv'
response = requests.get(url)
csv_content = response.text

# Mise en forme de la page
st.title('Bienvenue dans le meilleur des mondes')
