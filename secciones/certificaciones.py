import streamlit as st

def show():
    st.title("📜 Certificaciones")
    st.write("Aquí se encuentran algunas de mis certificaciones y logros académicos:")

    certificaciones = [
        {
            "titulo": "AWS Cloud Practitioner (Foundations)",
            "entidad": "Amazon Web Services",
            "fecha": "2024",
            "estado": "✅ Obtenido"
        },
        {
            "titulo": "AWS Certified Data Engineer",
            "entidad": "Amazon Web Services",
            "fecha": "2025",
            "estado": "✅ Obtenido"
        },
        {
            "titulo": "Certificado de Inglés (ITEP)",
            "entidad": "ITEP",
            "fecha": "2023",
            "detalle": "Nivel alcanzado: **B2 – C1**",
            "estado": "✅ Obtenido"
        },
        {
            "titulo": "Título Universitario – Ingeniería en Datos",
            "entidad": "Univerisada Politecnica de Yucatan",
            "fecha": "2025",
            "detalle": "Promedio general: **9.2 / 10**",
            "estado": "✅ Obtenido"
        }
    ]

    for cert in certificaciones:
        st.subheader(cert["titulo"])
        st.write(f"**Entidad:** {cert['entidad']}")
        st.write(f"**Fecha:** {cert['fecha']}")
        if "detalle" in cert:
            st.info(cert["detalle"])
        st.success(cert["estado"])
        st.markdown("---")
