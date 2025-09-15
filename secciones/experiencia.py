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
            - Desarrollo y mantenimiento de **scrapers robustos** para extracción automatizada de datos en diferentes portales, utilizando **Selenium** y **BeautifulSoup**, garantizando escalabilidad y reducción de errores manuales.  
            - Implementación de procesos de ingesta en **Dataiku**, diseñando flujos automáticos que permitieron **integrar y transformar datos de forma más eficiente**, reduciendo tiempos de carga y preparación.  
            - Colaboración estrecha con equipos multidisciplinarios (ingeniería, producto, negocio) para optimizar operaciones y asegurar que las soluciones de datos estuvieran alineadas con los **objetivos estratégicos de la organización**.  
            - **Resultado clave:** se mejoró la disponibilidad y calidad de los datos, habilitando análisis más confiables y decisiones de negocio mejor informadas.  
            """
        },
        {
            "puesto": "Data Engineer",
            "empresa": "Centro de Investigaciones Científicas de Yucatán",
            "periodo": "Febrero 2024 – Mayo 2024",
            "detalle": """
            - Diseño e implementación de **métodos innovadores de análisis de biomasa** a partir de imágenes satelitales, integrando **algoritmos de Machine Learning** para modelar la dinámica de ecosistemas.  
            - Construcción de **pipelines de limpieza y normalización de datos en Python**, reduciendo significativamente los tiempos de procesamiento y garantizando datasets de alta calidad para la investigación científica.  
            - Colaboración con investigadores para traducir resultados técnicos en **insights comprensibles y aplicables** en estudios medioambientales.  
            - **Resultado clave:** se aceleraron los ciclos de investigación al automatizar etapas críticas de preprocesamiento y análisis, sentando bases para proyectos futuros de monitoreo ambiental con datos geoespaciales.  
            """
        },
        {
            "puesto": "Data Analyst",
            "empresa": "Arithmos Data Science",
            "periodo": "Enero 2023 – Abril 2023",
            "detalle": """
            - Análisis de **datasets electorales** del estado de Oaxaca, correlacionando votos emitidos con indicadores socioeconómicos del **INEGI**.  
            - Identificación de **factores socioeconómicos clave** que influyen en la preferencia electoral y el nivel de participación ciudadana.  
            - Desarrollo de múltiples **visualizaciones estadísticas y gráficas interactivas** para mostrar patrones en la relación entre grupos sociales y partidos políticos.  
            - Uso de técnicas de correlación y análisis exploratorio para entender cómo variables como nivel educativo, ingresos y ocupación impactaban en las tendencias de voto.  

            **Resultados:**  
            - Generación de reportes claros y visuales para la toma de decisiones estratégicas.  
            - Presentación de hallazgos que mostraron relaciones significativas entre características demográficas y comportamiento electoral.  
            """
        }
    ]

    for exp in experiencias:
        st.subheader(f"{exp['puesto']} – {exp['empresa']}")
        st.write(f"**Periodo:** {exp['periodo']}")
        st.markdown(exp["detalle"])
        st.markdown("---")
