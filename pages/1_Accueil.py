import streamlit as st
from PIL import Image
import os

# --- Configuration de la page ---
st.set_page_config(layout="wide")

with st.sidebar:
    st.markdown(
        "<h3 style='color:#C9A86A;'>👋 Bienvenue sur mon portfolio Data</h3>",
        unsafe_allow_html=True
    )

# --- Titre principal (doré premium) ---
st.markdown(
    """
    <h1 style='color:#C9A86A; font-size:52px; margin-bottom:0px;'>
        François‑Xavier Lhermitte
    </h1>
    <p style='font-size:22px; margin-top:-10px; color:#cccccc;'>
        Data Analyst — Performance & Supply Chain
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- Mise en page : photo + texte ---
col1, col2 = st.columns([1, 2])

with col1:
    photo_path = os.path.join("assets", "photo_FX.jpg")
    if os.path.exists(photo_path):
        img = Image.open(photo_path)
        st.image(img, width=260)
    else:
        st.error("❌ Impossible de charger la photo. Vérifie le nom du fichier dans /assets.")

with col2:
    st.markdown(
        """
        <p style='font-size:19px; line-height:1.6;'>
        Après plus de vingt ans à piloter la performance Supply Chain, j’ai choisi de réorienter ma carrière vers la Data.  
        Ce pivot n’est pas un hasard : analyser, comprendre, optimiser… c’est ce que j’ai toujours fait.  
        Aujourd’hui, je mets cette expérience métier au service d’outils modernes, plus fiables, plus visuels, plus utiles.
        </p>

        <p style='font-size:19px; line-height:1.6;'>
        J’aime transformer des données brutes en décisions concrètes.  
        J’aime créer des tableaux de bord qui éclairent, pas qui compliquent.  
        Et surtout, j’aime comprendre les enjeux humains derrière les chiffres.
        </p>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# --- Présentation rapide (version premium) ---
colA, colB = st.columns([1, 2])

with colA:
    st.markdown(
        """
        <h3 style='color:#C9A86A;'>Profil</h3>
       
