import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Chargement des données
url = 'https://raw.githubusercontent.com/sole-tolo/Hackathon_Two/main/data_hack2.csv'
df = pd.read_csv(url)

# Fonction pour prédire le score
def predict_score(user_data):
    # Création du DataFrame utilisateur
    user_df = pd.DataFrame(user_data, index=[0])

    # Encodage des données utilisateur
    label_encoder = LabelEncoder()
    for colonne in user_df.columns:
        user_df[colonne] = label_encoder.fit_transform(user_df[colonne])

    # Définition des variables X et y
    X = df.drop(columns=['Score'])
    y = df['Score']  

    # Entraînement du modèle
    model = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)

    # Prédiction du score
    prediction = model.predict(user_df)

    return prediction[0]

# Mise en forme de la page
st.title('Bienvenue dans le meilleur des mondes')
st.header('Notez-vous les uns les autres')

# Définition des options pour les widgets
options = {
    'Niveau de diplôme': ['Bac', 'Bac +2', 'Bac +3', 'Bac +5', 'Doctorat', 'Pas de diplôme'],
    'Genre': ['Homme', 'Femme', 'Autre'],
    'Quartier': ['Centre-ville', 'Banlieue', 'Campagne'],
    'Classe sociale': ['Classe moyenne', 'Classe supérieure', 'Classe populaire'],
    'École des enfants': ['Privée', 'Publique'],
    'Dispose de femme de ménage': ['Oui', 'Non'],
    'Casier judiciaire': ['Vierge', 'Non vierge'],
    'Niveau social des parents': ['Bac', 'Bac +2', 'Bac +3', 'Bac +5', 'Doctorat', 'Pas de diplôme'],
    'Va souvent au cinéma': ['Oui', 'Non']
}

# Formulaire pour saisir les valeurs utilisateur
with st.form("Quelle est ta valeur?"):
    # Création des widgets
    user_data = {}
    for key, values in options.items():
        user_data[key] = st.selectbox(key, values)
    submitted = st.form_submit_button("Yes, you are gorgeous")

# Si le formulaire est soumis, faire la prédiction et afficher le résultat
if submitted:
    prediction = predict_score(user_data)
    st.write('Votre score prédit est :', prediction)



# import streamlit as st
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split


# # Chargement des données
# url = 'https://raw.githubusercontent.com/sole-tolo/Hackathon_Two/main/data_hack2.csv'
# df = pd.read_csv(url)

# # Mise en forme de la page
# st.title('Bienvenue dans le meilleur des mondes')
# st.header('Notez-vous les uns les autres')


# # je crée les widgets 

# options = {
#     'Niveau de diplôme': ['Bac', 'Bac +2', 'Bac +3', 'Bac +5', 'Doctorat', 'Pas de diplôme'],
#     'Genre': ['Homme', 'Femme', 'Autre'],
#     'Quartier': ['Centre-ville', 'Banlieue', 'Campagne'],
#     'Classe sociale': ['Classe moyenne', 'Classe supérieure', 'Classe populaire'],
#     'École des enfants': ['Privée', 'Publique'],
#     'Dispose de femme de ménage': ['Oui', 'Non'],
#     'Casier judiciaire': ['Vierge', 'Non vierge'],
#     'Niveau social des parents': ['Bac', 'Bac +2', 'Bac +3', 'Bac +5', 'Doctorat', 'Pas de diplôme'],
#     'Va souvent au cinéma': ['Oui', 'Non']
# }


# with st.form("Quelle est ta valeur?"):
# # je vais créer mes widgets
#     user_data = {}
#     for key, values in options.items():
#         user_data[key] = st.selectbox(key, values)
#     submitted = st.form_submit_button("Yes, you are gorgeous")

# # Si le formulaire est soumis je crée un df avec les données de l'utilisateur
# if submitted:
#     user_data_dict = {}
#     for key,value in user_data.items():
#         user_data_dict[key] = value
#     user_df = pd.DataFrame(user_data_dict)

#     # je défini mes variables 
#     X = df.drop(columns=['Score'])
#     y = df['Score']  

#     # j'encode les données pour l'algo
#     label_encoder = LabelEncoder()
#     for colonne in user_df.columns:
#         user_df[colonne] = label_encoder.fit_transform(user_df[colonne])

#     # Entraîner le modèle
#     model = LinearRegression()
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     model.fit(X_train, y_train)

#     # Faire une prédiction avec le modèle
#     prediction = model.predict(user_df)

#     st.write('Votre score prédit est :', prediction[0])