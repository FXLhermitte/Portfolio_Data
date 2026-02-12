import streamlit as st
import os

st.set_page_config(layout="wide")

# --- Titre ---
st.markdown("<h1 style='color:#C9A86A;'>Me Contacter</h1>", unsafe_allow_html=True)
st.write("Je suis toujours ouvert aux échanges autour de la Data, de la Supply Chain et des projets à impact.")

st.markdown("---")

# --- Coordonnées ---
st.markdown("## 📬 Mes coordonnées")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        ### 📧 Email  
        **elogaban@free.fr**

        ### 🔗 LinkedIn  
        [linkedin.com/in/françois-xavier-lhermitte](https://www.linkedin.com/in/fran%C3%A7ois-xavier-lhermitte-139108ba/)
        """
    )

with col2:
    st.markdown("### 📄 Mon CV")

    cv_path = "assets/CV_FX_Lhermitte.pdf"

    if os.path.exists(cv_path):
        with open(cv_path, "rb") as f:
            cv_bytes = f.read()

        st.download_button(
            label="📄 Télécharger mon CV",
            data=cv_bytes,
            file_name="CV_FX_Lhermitte.pdf",
            mime="application/pdf"
        )
    else:
        st.error("❌ CV introuvable. Vérifie le chemin : assets/CV_FX_Lhermitte.pdf")

st.markdown("---")

# --- Message final ---
st.markdown(
    """
    ## 🤝 Travaillons ensemble  
    Que ce soit pour un projet Data, un tableau de bord, une analyse ou un échange informel,  
    je serai ravi de discuter avec vous.
    """
)
