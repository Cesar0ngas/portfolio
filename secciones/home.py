import streamlit as st
from pathlib import Path

def show():
    st.title("Hola, soy Cesar Correa 👋🏽")
    st.header("Data Engineer")
    st.write(
        """
        Bienvenido a mi museo de proyectos. \n

        Actualmente me encuentro trabajando como IT Consultant haciendo proyectos de automatización, con la finalidad de reducir tiempo
        en actividades repetitivas y facilitar la visualización de información para la toma de decisiones. \n
        """
    )

    # Imagen de perfil + experiencia en columnas
    col1, col2 = st.columns([1, 3])
    profile_pic = Path("assets/img/yo.jpg")
    with col1:
        if profile_pic.exists():
            st.image(str(profile_pic), width=180)
    with col2:
        st.info("**+3 años de experiencia** en Ingeniería de Datos, trabajando en proyectos de automatización, análisis de información y soluciones en la nube.")

    # Sección: Sobre mí
    st.header("Sobre Mi")
    st.write(
        """
        - Experiencia en construcción de pipelines de datos, optimización de consultas SQL y dashboards.  
        - Manejo herramientas como **Python, SQL, Herramientas de Visualización**.  
        - Mi objetivo: crear soluciones que hagan los datos fáciles de entender y fáciles de obtener, ahorrando tiempo y mejorando la eficiencia.  
        """
    )

    # Sección: Habilidades Técnicas
    st.header("Habilidades Técnicas")
    cols = st.columns(3)

    with cols[0]:
        st.markdown("**Lenguajes de Programación**")
        st.write(
            """
            - Python
            - R
            - SQL
            - Nest
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
            - ETL/ELT (Beautiful Soup, Selenium)  
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
