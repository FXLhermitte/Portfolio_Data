import streamlit as st
from PIL import Image
import os

st.set_page_config(layout="wide")

# --- Titre ---
st.markdown("<h1 style='color:#C9A86A;'>Quelques réalisations</h1>", unsafe_allow_html=True)
st.write("Des analyses concrètes, construites avec rigueur et racontées avec sens.")

st.markdown("---")

def show_image(filename):
    path = os.path.join("assets", filename)
    if os.path.exists(path):
        img = Image.open(path)
        st.image(img)
    else:
        st.error(f"❌ Image introuvable : {filename}")


# ---------------------------------------------------------
# 🌍 PROJET 1 — Réchauffement climatique
# ---------------------------------------------------------
st.markdown("## 🌍 Réchauffement climatique — Analyse Python")

st.markdown(
    """
    Nettoyage de datasets en Python :
    
    https://colab.research.google.com/drive/1qaAKH4bK7vBUU8rh-6oP26rNbtxclPpE#scrollTo=651231cc-2925-4fbd-ad5f-29e2724fff1e
    https://colab.research.google.com/drive/1SrkLBAjnYfSsqKXETLm3julWP9AsEAhQ#scrollTo=uVzyNRzqOdKZ

    Un projet qui m’a marqué, parce qu’il relie la donnée à un enjeu humain et global.  
    J’ai travaillé sur l’évolution des températures, la visualisation des tendances,  
    et la mise en évidence de signaux faibles.  
    Ce projet m’a rappelé que derrière chaque dataset, il y a une histoire à raconter.
    """
)

# Liste des images
images_climat = [
    "Climat_1.png", "Climat_2.png", "Climat_3.png", "Climat_4.png",
    "Climat_5.png", "Climat_6.png", "Climat_7.png", "Climat_8.png"
]

# 3 colonnes pour 8 images
cols = st.columns(3)

for i, img in enumerate(images_climat):
    with cols[i % 3]:
        show_image(img)

st.markdown("---")

# ---------------------------------------------------------
# 📞 PROJET 2 — Call Center
# ---------------------------------------------------------
st.markdown("## 📞 Call Center — Analyse volumétrique")

st.markdown(
    """
    Ici, j’ai analysé les volumes d’appels, les pics d’activité et les temps de réponse.  
    Ce projet m’a permis de montrer comment la donnée peut améliorer l’expérience client  
    et optimiser l’organisation d’une équipe opérationnelle.
    """
)

images_call = [
    "Call_center_1.png",
    "Call_center_2.png",
    "Call_center_3.png"
]

cols = st.columns(2)

for i, img in enumerate(images_call):
    with cols[i % 2]:
        show_image(img)

st.markdown("---")


# ---------------------------------------------------------
# 📊 PROJET 3 — Distrib Nord (Power BI)
# ---------------------------------------------------------
st.markdown("## 📊 Distrib Nord — Tableau de bord Power BI")

st.markdown(
    """
    Un projet très visuel, construit autour de la performance commerciale.  
    J’ai conçu un tableau de bord clair, orienté décision,  
    pour aider un manager à piloter ses indicateurs clés en un coup d’œil.
    """
)

images_distrib = [
    "Distrib_Nord_1.png",
    "Distrib_Nord_2.png",
    "Distrib_Nord_3.png",
    "Distrib_Nord_4.png"
]

cols = st.columns(2)

for i, img in enumerate(images_distrib):
    with cols[i % 2]:
        show_image(img)

st.markdown("---")


# ---------------------------------------------------------
# 📈 PROJET 4 — Suivi des ventes
# ---------------------------------------------------------
st.markdown("## 📈 Suivi des ventes — Analyse commerciale")

st.markdown(
    """
    Une analyse simple mais essentielle : comprendre les dynamiques de vente,  
    identifier les produits moteurs, et détecter les signaux faibles.  
    Ce projet montre ma capacité à relier la donnée au terrain.
    """
)

images_ventes = [
    "Suivi_ventes_1.png",
    "Suivi_ventes_2.png"
]

cols = st.columns(2)

for i, img in enumerate(images_ventes):
    with cols[i % 2]:
        show_image(img)


st.markdown("---")


