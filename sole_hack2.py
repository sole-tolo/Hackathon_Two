import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Chargement des données
url = 'https://raw.githubusercontent.com/sole-tolo/Hackathon_Two/main/data_hack2.csv'
df = pd.read_csv(url)

# Mise en forme de la page
st.title("Et maintenant, vote pour tes ami.e.s")

# Conteneur de colonnes pour ajuster la mise en page
col1, col2 = st.columns([1, 3])

# Contenu de la première colonne (image)
with col1:
    # Image alignée à gauche
    image_path = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Black_Mirror_logo.svg/1200px-Black_Mirror_logo.svg.png"
    st.image(image_path, caption="Your Image", use_column_width=True)

# Contenu de la deuxième colonne (texte)
with col2:
    # Titre et description
    st.write("# A toi de jouer")
    

# Initialisation du score
score = 0

# Création du formulaire
with st.form("evaluation_form"):
    # Question 1: Allumé la caméra pendant les présentations?
    camera_on = st.radio("A-t-il ou elle allumé la caméra pendant les présentations?", ("Oui", "Non"))
    if camera_on == "Oui":
        score += 0.5

    # Question 2: Sourit-il pendant les présentations des autres?
    smiling = st.radio("Sourit-il ou elle pendant les présentations des autres?", ("Oui", "Non"))
    if smiling == "Oui":
        score += 0.5

    # Question 3 (ton camarade est il bien habillé?
    dressing = st.radio(" Est-il ou elle bien habillé.e pour l'occasion?",("Oui", "Non"))
    if  dressing == 'Oui':
        score += 0.3

    # Question 4: Penses-tu que ton collègue est violent?
    violence = st.radio("Ton ou ta camarade montre des signes,même légers, de violence ou impolitesse?", ("Oui", "Non"))
    if violence == "Oui":
        score -= 0.3

    # Question 5: Langage inclusif?
    inclusif = st.radio("Est-ce que ton ou ta camarade parle en langage inclusif?", ("Oui", "Non"))
    if inclusif =="Oui":
        score-= 0.1

    # Soumission du formulaire
    submit_button = st.form_submit_button("Submit")

# Affichage du score final après la soumission du formulaire
if submit_button:
    st.write(f"Score final: {score} sur 3")
    st.write("Ton ami.e a été évalué.e! Félicitations!")
    image_path ='https://cdn-icons-png.flaticon.com/512/889/889140.png'
    st.image(image_path)
    # Réinitialisation du score
    score = 0
    camera_on = None
    smiling = None
    credible_decor = None
    violence = None
    inclusif = None

# Contenu dans la barre latérale à gauche
with st.sidebar:
    st.title('Quelle est ta valeur de base?')
    
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

        # Afficher la prédiction
        st.markdown('## Ta valeur de base est :')
        st.image('https://cdn-icons-png.flaticon.com/512/889/889140.png', width=100)
        st.write(f'Ta valeur de base est {prediction[0]:.2f}**')
        # # Afficher la prédiction
        # st.write('Votre score prédit est :', prediction[0])
        # Afficher la prédiction au centre de la page
   