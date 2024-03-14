import streamlit as st
import pandas as pd
import requests
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# Chargement des données
url = 'https://raw.githubusercontent.com/sole-tolo/Hackathon_Two/main/data_hack2.csv'
df = pd.read_csv(url)

# Mise en forme de la page
st.title('Bienvenue dans le meilleur des mondes')
st.header('Notez-vous les uns les autres')

# interface utilisateur
niveau_diplome = st.selectbox('Niveau de diplôme', ['Bac', 'Bac +2', 'Bac +3', 'Bac +5', 'Doctorat', 'Pas de diplôme'])
genre = st.selectbox('Genre', ['Homme', 'Femme', 'Autre'])
quartier = st.selectbox('Quartier', ['Centre-ville', 'Banlieue', 'Campagne'])
classe_sociale = st.selectbox('Classe sociale', ['Classe moyenne', 'Classe supérieure', 'Classe populaire'])
ecole_enfants = st.selectbox('École des enfants', ['Privée', 'Publique'])
femme_menage = st.selectbox('Dispose de femme de ménage', ['Oui', 'Non'])
casier_judiciaire = st.selectbox('Casier judiciaire', ['Vierge', 'Non vierge'])
niveau_social_parents = st.selectbox('Niveau social des parents', ['Bac', 'Bac +2', 'Bac +3', 'Bac +5', 'Doctorat', 'Pas de diplôme'])
cinema = st.radio('Va souvent au cinéma', ['Oui', 'Non'])