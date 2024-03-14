import streamlit as st
import pandas as pd
import requests

# Chargement des données
url = 'https://github.com/sole-tolo/Hackathon_Two/blob/main/data_hack2.csv'
response = requests.get(url)
csv_content = response.text

# Mise en forme de la page
st.title('Bienvenue dans le meilleur des mondes')
st.write("Notez-vous les uns les autres")
s
t.title("Tu es seul.e pour cette Saint Valentin? Tu ne sais pas quoi manger, ni quoi écouter.. bref, tu es perdu.e?")
st.header("Ici on t'aide avec quelques tips un peu bidon")
# st.image(lien_image2)
col1, col2,col3 = st.columns([1, 3, 1])
col1.write("")
image_path = "https://www.kideaz.com/wp-content/uploads/elementor/thumbs/moufles-couple-350-450-o8ist9xtyb036k7n6zgp5yv6igi8uvnrzmi24z5c74.jpg"
col2.image(image_path, caption="Your Image", use_column_width=True)
col2.write("")
col3.write("")
