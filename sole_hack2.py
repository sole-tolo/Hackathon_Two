import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Chargement des données
url = 'https://raw.githubusercontent.com/sole-tolo/Hackathon_Two/main/data_hack2.csv'
df = pd.read_csv(url)

# Mise en forme de la page
st.title('Bienvenue dans le meilleur des mondes')
st.header('Notez-vous les uns les autres')

# Contenu principal centré
col1, col2, col3 = st.columns([1, 3, 1])

# Affichage du titre, de l'en-tête et de l'image dans la partie centrale
with col2:
    image_path = "https://static.wixstatic.com/media/ede727_f05b8b1ac9f74d8ea06caac1590ad3e3~mv2.jpeg/v1/fill/w_1000,h_524,al_c,q_85,usm_0.66_1.00_0.01/ede727_f05b8b1ac9f74d8ea06caac1590ad3e3~mv2.jpeg"
    st.image(image_path, caption="Your Image", use_column_width=800)
    st.header('Prenez quelques minutes pour découvrir TOP5, notre nouveau système de notation du bonheur')

# Contenu dans la barre latérale à gauche
with st.sidebar:
    st.title('Formulaire')
    
    # Création des widgets
    options = {
        'Niveau de diplôme': ['Bac', 'Bac +2', 'Bac +3', 'Bac +5', 'Doctorat', 'Pas de diplôme'],
        'Quartier': ['Centre-ville', 'Banlieue', 'Campagne'],
        'Classe sociale': ['Classe moyenne', 'Classe supérieure', 'Classe populaire'],
        'École des enfants': ['Privée', 'Publique'],
        'Dispose de femme de ménage': ['Oui', 'Non'],
        'Casier judiciaire': ['Vierge', 'Non vierge'],
        'Niveau social des parents': ['Bac', 'Bac +2', 'Bac +3', 'Bac +5', 'Doctorat', 'Pas de diplôme'],
        'Va souvent au cinéma': ['Oui', 'Non']
    }

    with st.form("Quelle est ta valeur?"):
        # Création des widgets
        user_data = {'Niveau de diplôme':'','Quartier':'','Salaire(€)':0,'Classe sociale':'','École des enfants':'','Dispose de femme de ménage':'', 
                     "Prix au mètre carré de l'habitation(€/m2)":0,'Casier judiciaire':'',"Niveau social des parents":"",'Va souvent au cinéma':""}
        user_data['Salaire(€)'] =st.number_input("Salaire(€)")
        user_data["Prix au mètre carré de l'habitation(€/m2)"] =st.number_input("prix au m2 de ton lieu d'habitation")

        for key, values in options.items():
            user_data[key] = st.selectbox(key, values)
        submitted = st.form_submit_button("Yes, you are gorgeous")

    # Si le formulaire est soumis, afficher les prédictions
    if submitted:
        # Création du DataFrame avec les données utilisateur
        user_data_dict = {}
        for key, value in user_data.items():
            user_data_dict[key] = value
        user_df = pd.DataFrame([user_data_dict], index=[0])  # Spécifier l'index pour une seule ligne de données

        # j'encode les données utilisateur avec les mêmes catégories que celles de la df d'entraînement
        label_encoder = LabelEncoder()

        for colonne in user_df.select_dtypes(include=['object']).columns:
            user_df[colonne] = label_encoder.fit(user_df[colonne]).transform(user_df[colonne])

        # je défini mes variables 
        X = df.drop(columns=['Score','Age','Genre'])
        y = df['Score']  

        # Entraîner le modèle
        model = LinearRegression()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_train, y_train)

        # Faire une prédiction avec le modèle
        prediction = model.predict(user_df)

        # Afficher les scores R² du modèle sur les ensembles d'entraînement et de test
        st.write(model.score(X_train, y_train))
        st.write(model.score(X_test, y_test))

        # Afficher la prédiction
        st.write('Votre score prédit est :', prediction[0])