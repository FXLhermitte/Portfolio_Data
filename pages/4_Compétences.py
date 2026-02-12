import streamlit as st

st.set_page_config(layout="wide")

# --- Titre ---
st.markdown("<h1 style='color:#C9A86A;'>Mes Compétences</h1>", unsafe_allow_html=True)
st.write("Une expertise solide, à la croisée de la Data et de la Supply Chain.")

st.markdown("---")

# ---------------------------------------------------------
# 🧠 COMPÉTENCES DATA
# ---------------------------------------------------------
st.markdown("## 🧠 Compétences Data")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        ### **Python**
        - Manipulation de données (Pandas)  
        - Visualisation (Matplotlib, Seaborn)  
        - Nettoyage, préparation, transformation  
        - Analyse exploratoire  
        """
    )

    st.markdown(
        """
        ### **SQL**
        - Jointures complexes  
        - CTE et sous‑requêtes  
        - Agrégations et fenêtres  
        - Optimisation et lisibilité des requêtes  
        """
    )

with col2:
    st.markdown(
        """
        ### **Power BI**
        - Modélisation de données  
        - Mesures DAX  
        - Tableaux de bord orientés décision  
        - Design clair et professionnel  
        """
    )

    st.markdown(
        """
        ### **Machine Learning**
        - Régressions  
        - Arbres de décision  
        - Clustering  
        - Validation et interprétation des modèles  
        """
    )

st.markdown("---")

# ---------------------------------------------------------
# 🚚 COMPÉTENCES SUPPLY CHAIN
# ---------------------------------------------------------
st.markdown("## 🚚 Compétences Supply Chain")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        ### **Pilotage de la performance**
        - Suivi d’indicateurs clés  
        - Analyse des écarts  
        - Plans d’action  
        """
    )

    st.markdown(
        """
        ### **S&OP / Prévisions**
        - Coordination des acteurs  
        - Construction de plans fiables  
        - Arbitrages et scénarios  
        """
    )

with col2:
    st.markdown(
        """
        ### **Optimisation des flux**
        - Approvisionnement  
        - Logistique  
        - Coordination multisites  
        """
    )

    st.markdown(
        """
        ### **Management**
        - Encadrement d’équipes  
        - Accompagnement et montée en compétence  
        - Animation et communication  
        """
    )

st.markdown("---")

# ---------------------------------------------------------
# 🎯 COMPÉTENCES TRANSVERSES
# ---------------------------------------------------------
st.markdown("## 🎯 Compétences transverses")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        ### **Gestion de projet**
        - Structuration  
        - Planification  
        - Suivi et livraison  
        """
    )

    st.markdown(
        """
        ### **Communication**
        - Vulgarisation  
        - Présentations claires  
        - Adaptation au public  
        """
    )

with col2:
    st.markdown(
        """
        ### **Résolution de problèmes**
        - Analyse structurée  
        - Recherche de solutions  
        - Prise de décision  
        """
    )

    st.markdown(
        """
        ### **Esprit d’équipe**
        - Collaboration  
        - Fiabilité  
        - Sens du collectif  
        """
    )