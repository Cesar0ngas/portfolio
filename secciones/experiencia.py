import streamlit as st

def show():
    st.title("💼 Experiencia Profesional")
    st.write("Aquí encontrarás mi experiencia laboral más relevante y proyectos destacados en cada rol.")

    experiencias = [
        {
            "puesto": "IT Consultant",
            "empresa": "Basteris Reyes & Asociados",
            "periodo": "Enero 2025 – Actualidad",
            "detalle": """
            - Desarrollo de herramienta en **Python** para consolidación de libros XML contables, reduciendo tiempos de horas a minutos.  
            - Creación de **plataforma de identificación de partes relacionadas** usando **NestJS, React+Vite, AWS S3/EC2 y MongoDB Atlas**, entregando resultados en minutos.  
            - Integración de **Wisesheets con Excel** para extracción y análisis financiero.  
            - Desarrollo de **apps internas con AppSheet y Looker Studio** para apoyar la toma de decisiones.  

            **Proyectos clave:**  
            - Inicio del proyecto **SATisFACTURE**.  
            - Implementación de soluciones de automatización para clientes corporativos.  
            """
        },
        {
            "puesto": "Data Engineer",
            "empresa": "Plenumsoft",
            "periodo": "Mayo 2024 – Agosto 2024",
            "detalle": """
            - Desarrollo y mantenimiento de scrapers para extracción de datos automatizada.  
            - Implementación de procesos de ingesta en **Dataiku** con flujos automáticos.  
            - Colaboración con equipos multidisciplinarios para optimizar eficiencia operativa.  
            """
        },
        {
            "puesto": "Data Engineer",
            "empresa": "Centro de Investigaciones Científicas de Yucatán",
            "periodo": "Febrero 2024 – Mayo 2024",
            "detalle": """
            - Implementación de métodos de análisis de biomasa con datos satelitales y algoritmos de **Machine Learning**.  
            - Desarrollo de scripts en **Python** para limpieza de datos y reducción significativa de tiempos de procesamiento.  
            """
        }
    ]

    for exp in experiencias:
        st.subheader(f"{exp['puesto']} – {exp['empresa']}")
        st.write(f"**Periodo:** {exp['periodo']}")
        st.markdown(exp["detalle"])
        st.markdown("---")
