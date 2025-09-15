import streamlit as st

def show():
    st.title("📜 Certificaciones")
    st.write("Aquí se encuentran algunas de mis certificaciones y logros académicos:")

    certificaciones = [
        {
            "titulo": "AWS Certified Data Engineer",
            "entidad": "Amazon Web Services",
            "fecha": "2025",
            "detalle": None,
            "estado": "✅ Obtenido",
            "link": "https://www.credly.com/badges/224969fd-0482-4f9f-80ac-cf800277b342/linked_in_profile"
        },
        {
            "titulo": "AWS Cloud Practitioner (Foundations)",
            "entidad": "Amazon Web Services",
            "fecha": "2024",
            "detalle": None,
            "estado": "✅ Obtenido",
            "link": "https://www.credly.com/badges/8fbae699-8153-4e6c-ac4c-0d3914d8c504/linked_in_profile"
        },
        {
            "titulo": "Certificado de Inglés (ITEP)",
            "entidad": "ITEP",
            "fecha": "2023",
            "detalle": "Nivel alcanzado: **B2 – C1**",
            "estado": "✅ Obtenido",
            "link": None
        },
        {
            "titulo": "Título Universitario – Ingeniería en Datos",
            "entidad": "Universidad Politécnica de Yucatán",
            "fecha": "2025",
            "detalle": "Promedio general: **9.2 / 10**",
            "estado": "✅ Obtenido",
            "link": None
        }
    ]

    for cert in certificaciones:
        st.subheader(cert["titulo"])
        st.write(f"**Entidad:** {cert['entidad']}")
        st.write(f"**Fecha:** {cert['fecha']}")
        if "detalle" in cert and cert["detalle"]:
            st.info(cert["detalle"])
        if cert["link"]:
            st.markdown(f"[🔗 Ver credencial oficial]({cert['link']})")
        st.success(cert["estado"])
        st.markdown("---")
