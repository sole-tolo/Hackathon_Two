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

# Créer une interface utilisateur pour saisir les données personnelles
input_public = {}
for colonne in df.columns:
    if colonne != 'Score':
        valeur = st.text_input(colonne, "")
        input_public[colonne] = valeur

# # Algo de recommandation
# label_encoder = LabelEncoder()
# for colonne in df.columns:
#     if colonne != 'Score':
#         input_public[colonne] = label_encoder.fit_transform([input_public[colonne]])[0]

# X = df.drop(columns=['Score'])
# y = df['Score']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model = LinearRegression()
# model.fit(X_train, y_train)

# prediction = model.predict([list(input_public.values())])

# st.write("Score prédit :", prediction[0])

