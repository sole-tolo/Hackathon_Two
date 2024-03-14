import streamlit as st
import pandas as pd

# Chargement des données
file_path = r"C:\Users\solea\Desktop\Hackathon2\data_hack2.csv"
df = pd.read_csv(file_path)

# Deco page
st.title('Bienvenu.es dans le meilleurs des mondes')
st.write ( "Notez-vous les uns les autres")