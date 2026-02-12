import streamlit as st

st.set_page_config(layout="wide")

# --- Animation fade-in ---
st.markdown("""
<style>
.fade-in {
    animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(10px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# --- Titre ---
st.markdown("<h1 style='color:#C9A86A;'>Mon Parcours</h1>", unsafe_allow_html=True)
st.write("Une trajectoire guidée par la performance, l’humain et la donnée.")

st.markdown("---")

# --- Sous-titre ---
st.markdown("## 📌 Mon histoire professionnelle")

# Fonction utilitaire pour un bloc de timeline
def timeline_block(date, title, text):
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 0.1, 6])

    with col1:
        st.markdown(
            f"<p style='text-align:right; font-weight:bold; font-size:18px;'>{date}</p>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            "<div style='border-left: 3px solid #C9A86A; height: 100%; margin-left: 8px;'></div>",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(f"### {title}")
        st.write(text)
        st.markdown("")

    st.markdown('</div>', unsafe_allow_html=True)

# --- Timeline complète ---

timeline_block(
    "2025",
    "**Data Analyst (Datascientest / Mines Paris)**",
    "Après plus de vingt ans en Supply Chain, j’ai choisi de me réinventer. "
    "Cette formation a été un tournant : Python, SQL, Power BI, Machine Learning… "
    "J’y ai retrouvé ce que j’aime : comprendre, analyser, transformer."
)

timeline_block(
    "2014 – 2024",
    "**Manager Supply Chain (Leroy Merlin)**",
    "Dix années à piloter la performance à l’échelle nationale. "
    "J’ai coordonné des équipes pluridisciplinaires, fiabilisé les données, automatisé des reportings, "
    "et contribué à la digitalisation des processus logistiques. "
    "C’est là que j’ai compris que la donnée n’était pas un outil : c’était un levier stratégique."
)

timeline_block(
    "2006 – 2014",
    "**Responsable Groupe Approvisionnement**",
    "Management, coordination multisites, optimisation des flux. "
    "J’ai appris à prendre du recul, à structurer, à anticiper. "
    "Des compétences qui résonnent aujourd’hui dans mon travail de Data Analyst."
)

timeline_block(
    "2003 – 2006",
    "**Coordinateur Logistique**",
    "Négociation, mise en œuvre de solutions logistiques, pilotage opérationnel. "
    "Le terrain m’a appris la rigueur, la réactivité et la compréhension fine des enjeux business."
)

timeline_block(
    "1996 – 2003",
    "**Approvisionneur**",
    "Mes débuts dans la Supply Chain. "
    "C’est là que j’ai découvert le plaisir d’optimiser, d’améliorer, de résoudre."
)

st.markdown("---")

# --- Ce que tu apportes ---
st.markdown("## 🎯 Ce que j’apporte aujourd’hui")

st.write(
    "Avec ce parcours, je ne viens pas seulement avec des compétences techniques. "
    "Je viens avec **20 ans de compréhension du terrain**, des équipes, des contraintes, des enjeux. "
    "Je sais lire une donnée, mais surtout je sais **ce qu’elle signifie** pour un métier, un client, une organisation."
)