import streamlit as st
import pandas as pd
import requests
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# Chargement des données
url = 'https://github.com/sole-tolo/Hackathon_Two/blob/main/data_hack2.csv'
df = pd.read_csv(url)

# Mise en forme de la page
st.title('Bienvenue dans le meilleur des mondes')
st.header('Notez-vous les uns les autres')
