import streamlit as st
from pathlib import Path

def show():
    st.title("Hola, soy Cesar Correa 👋🏽")
    st.header("Data Engineer | ETL | SQL | ML | Data Visualization | Optimization & Automation")
    st.write(
        """
        Bienvenido a mi museo de proyectos. \n

        Actualmente me encuentro trabajando como IT Consultant haciendo proyectos de automatizacion, con la finalidad de reducir tiempo
        en actividades repetitivas y facilitar la visualizacion de informacion para la toma de decisiones. \n
        """
    )

    # Imagen de perfil
    profile_pic = Path("assets/img/yo.jpg")
    if profile_pic.exists():
        st.image(str(profile_pic), width=180)

    # Sección: Sobre mí
    st.header("Sobre Mi")
    st.write(
        """
        - Experiencia en construcción de pipelines de datos, optimización de consultas SQL y dashboards.
        - Manejo herramientas como **Python, SQL, Herramientas de Visualizacion**.
        - Mi objetivo: crear soluciones que hagan los datos fáciles de entender y faciles de obtener manteniendo flujos de datos, ahorrando tiempo y mejorando la eficienia.
        """
    )

    # Sección: Habilidades Técnicas
    st.header("Habilidades Tecnicas")
    cols = st.columns(3)

    with cols[0]:
        st.markdown("**Lenguajes de Programacion**")
        st.write(
            """
            - Python
            - R
            - SQL
            - Javascript
            - CSS
            - React
            - Excel
            """
        )

    with cols[1]:
        st.markdown("**Data**")
        st.write(
            """
            - DBMS (MongoDB, Dynamo, SQL Server)
            - AWS (EC2, S3, Lambda, CloudWatch, EventBridge)
            - Docker
            - Postman
            - Kafka
            - Data Manipulation (Pandas, Polars)
            - Data Visualization (PowerBI, Tableau, LookerStudio, Matplotlib, Seaborn)
            """
        )

    with cols[2]:
        st.markdown("**Apps**")
        st.write(
            """
            - PowerApps
            - PowerAutomate
            - Appsheets
            - Bots w/ Appsheets
            """
        )

    # Sección: Contacto
    st.header("Contacto")
    st.write(
        """
        - **LinkedIn:** https://www.linkedin.com/in/cesar-correa-45074a294/
        - **Correo:** cescor.0503@gmail.com
        - **GitHub:** https://github.com/Cesar0ngas
        """
    )
