import streamlit as st
from secciones import home, proyectos, certificaciones, experiencia

st.set_page_config(page_title="Portfolio - Cesar Correa", layout="wide")

menu = st.sidebar.selectbox(
    "📌 Navegación",
    ["Home", "Proyectos", "Experiencia", "Certificaciones"]
)

if menu == "Home":
    home.show()

elif menu == "Proyectos":
    proyectos.show()

elif menu == "Certificaciones":
    certificaciones.show()

elif menu == "Experiencia":
    experiencia.show()

