import streamlit as st

def show():
    st.title("📂 Proyectos")
    st.write(
        """
        En esta sección encontrarás algunos proyectos que considero importantes en los que he participado
        y algunos que he encabezado.
        """
    )

    proyectos = [
        {
            "titulo": "SATisFACTURE",
            "descripcion": "Implementación de API para la descarga masiva de CFDIs y Metadata desde el SAT.",
            "estado": "En curso",
            "repositorio": None,
            "imagen": None,
            "detalle": """

            Proyecto en desarrollo para la descarga masiva de CFDIs y Metadata desde el SAT, con autenticación mediante FIEL
            y almacenamiento seguro en la nube.  

            **Fechas:**  
            - Inicio: Marzo 2025  
            - Finalización estimada: Diciembre 2025 (uso en producción desde Marzo 2026)  

            **Proceso principal (5 pasos):**
            1. Autenticación con la FIEL del cliente.  
            2. Solicitudes individuales o de ejercicio completo (64 solicitudes en un solo click).  
            3. Verificación de solicitudes ante el SAT.  
            4. Descarga de paquetes de CFDIs y Metadata.  
            5. Procesamiento y almacenamiento de la información en MongoDB.  

            **Tecnologías usadas / planeadas:**  
            - Python, FastAPI  
            - AWS S3 (almacenamiento), EC2 / Lambda (ejecución), EventBridge (automatización)  
            - MongoDB  
            - Postman (pruebas de endpoints)  

            **Estado:** 🛠️ En pruebas, con meta de producción en 2026.
            """
        },
        {
            "titulo": "Cash Management App",
            "descripcion": "Aplicación para gestión del flujo de efectivo con protocolos de seguridad según el rol del usuario.",
            "estado": "Finalizado",
            "repositorio": None,
            "imagen": None,
            "detalle": """

            Aplicación desarrollada en **AppSheet** para gestionar el flujo de efectivo de manera controlada y organizada.  

            **Fechas:**  
            - Inicio: Junio 2025  
            - Finalización: Agosto 2025  

            **Problemática:**  
            El cliente llevaba el control de efectivo de forma no organizada, generando inconsistencias.  

            **Solución:**  
            Una aplicación intuitiva en AppSheet con roles diferenciados:  
            - **Admin:** acceso total y descargas de movimientos.  
            - **Responsable:** asignado a una o varias UDN, puede registrar usuarios.  
            - **Intermediario:** solo puede redirigir o reenviar movimientos.  

            **Características clave:**  
            - Validación de cada movimiento con código enviado por correo.  
            - Seguridad y privacidad según rol y unidad de negocio.  
            - Opción de reenviar códigos si se pierden.  
            - Próxima fase: análisis interactivo en **Looker Studio**.  

            **Tecnologías:**  
            - AppSheet  
            - Supabase  
            - Looker Studio (planeado)
            """
        },
        {
            "titulo": "CFDI Automatization",
            "descripcion": "Automatización del procesamiento de CFDIs descargados, con análisis de precios de transferencia.",
            "estado": "Finalizado",
            "repositorio": None,
            "imagen": None,
            "detalle": """

            Proyecto relacionado con **SATisFACTURE**, enfocado en el **procesamiento eficiente de CFDIs** descargados desde el SAT.  

            **Fechas:**  
            - Inicio: Enero 2025  
            - Finalización: Marzo 2025  

            **Funcionamiento:**  
            - Subida de archivos `.zip` con XMLs de facturas emitidas y recibidas.  
            - Subida de archivo Excel con RFCs de empresas relacionadas.  
            - Procesamiento de XMLs para extraer campos clave (UUID, RFCs, conceptos, impuestos, etc.).  
            - Procesamiento **en paralelo** para reducir el tiempo de análisis a **menos de 5 minutos**.  
            - Identificación de operaciones entre partes relacionadas para análisis de precios de transferencia.  

            **Resultados:**  
            - Reducción del tiempo de análisis manual en un **70%**.  
            - Base sólida para integrarse con **SATisFACTURE** y automatizar todo el flujo.  

            **Tecnologías usadas:**  
            - **Frontend:** React + Vite (hospedado en Vercel)  
            - **Backend:** Ejecutado en AWS EC2  
            - **Almacenamiento:** AWS S3, MongoDB  
            - **Procesamiento:** Javascript + ejecución en paralelo para acelerar la lectura de XMLs  
            """
        }
        ,
        {
            "titulo": "FaceRecognition Attendance",
            "descripcion": "Sistema de control de asistencia basado en reconocimiento facial.",
            "estado": "Finalizado",
            "repositorio": None,
            "imagen": None,
            "detalle": """

            Proyecto de visión por computadora que utiliza reconocimiento facial para registrar asistencia.  

            **Fechas:**  
            - Inicio: Noviembre 2024  
            - Finalización estimada: Noviembre 2024 


            **Qué se hizo:**  
            - Se entrenó un modelo de reconocimiento facial usando **keras-facenet** para generar embeddings faciales de imágenes etiquetadas.  
            - Se utilizó un **label encoder** para asignar identificadores (IDs) a los usuarios, y un clasificador SVM con **sklearn** para distinguir rostros basado en los embeddings.  
            - Se desplegó el modelo como endpoint en **Azure ML** para que la parte de inferencia (reconocer rostros nuevos) fuera remota y escalable.  
            - Se desarrolló la interfaz de usuario con **Streamlit**, permitiendo tomar fotos, identificar usuario, mostrar historial, etc.  
            - Los datos (imágenes, información de los estudiantes) se almacenan en **MongoDB Atlas**.  

            **Tecnologías usadas:**  
            - Python, keras-facenet, sklearn, joblib  
            - Azure ML para endpoint de inferencia  
            - Streamlit para interfaz web  
            - MongoDB Atlas para base de datos de estudiantes  

            **Aprendizajes y resultados clave:**  
            - Comprensión profunda de embeddings faciales y cómo manejar identificación de rostros en condiciones reales.  
            - Manejo de bugs relacionados con compatibilidad de entorno en Azure (por ejemplo versión de Python).  
            - Logística de almacenamiento de imágenes e información personal de forma segura.  
            - Experiencia en despliegue de modelo a producción, integrando front-end y back-end.  
            """
        },
        {
            "titulo": "WALMEX Stock Analysis",
            "descripcion": "Sistema de análisis financiero que identifica momentos de entrada/salida usando EMA de 20 días, complementado con modelos de series temporales (ARIMA/SARIMA).",
            "estado": "En curso",
            "repositorio": None,
            "imagen": None,
            "detalle": """
            ### Predicción de puntos de entrada y salida con EMA + ARIMA/SARIMA  

            Este proyecto combina indicadores técnicos y modelos estadísticos para analizar series temporales financieras y **detectar puntos óptimos de entrada y salida**.  

            **Fechas:**  
            - Inicio: Octubre 2023  
            - Finalización estimada: En curso

            **Objetivos principales:**  
            - Usar la **Media Móvil Exponencial (EMA 20 días)** para marcar señales de compra/venta.  
            - Implementar modelos de series temporales (**ARIMA y SARIMA**) para predecir tendencias a corto y mediano plazo.  
            - Añadir “escudos” o filtros que protejan frente a señales falsas (ej. volumen, volatilidad).  

            **Resultados actuales:**  
            - Identificación más precisa de ventanas de entrada y salida comparado con EMA pura.  
            - Reducción de falsos positivos gracias al cruce entre predicciones estadísticas y técnicas.  
            - Visualizaciones que muestran retrocesos históricos y puntos sugeridos de acción.  

            **Tecnologías usadas:**  
            - Python (Pandas, NumPy, Statsmodels, Scikit-learn)  
            - Visualización: Matplotlib, Seaborn, Plotly  
            - Modelos estadísticos: ARIMA y SARIMA para series temporales  

            **Próximos pasos:**  
            - Integrar **sentiment analysis** de redes sociales (ej. Twitter/X) para incorporar señales basadas en el sentimiento del mercado.  
            - Explorar el uso de NLP y modelos preentrenados para capturar correlaciones entre noticias y movimientos de precio.  
            """
        }
    ]

    # Estado inicial
    if "proyecto_actual" not in st.session_state:
        st.session_state["proyecto_actual"] = None

    # Vista general
    if st.session_state["proyecto_actual"] is None:
        for proyecto in proyectos:
            st.subheader(proyecto["titulo"])

            cols = st.columns([1, 3])

            if proyecto["imagen"]:
                try:
                    cols[0].image(proyecto["imagen"], use_container_width=True)
                except:
                    cols[0].write("📷 Sin imagen")
            else:
                cols[0].write("📷")

            with cols[1]:
                st.write(proyecto["descripcion"] or "Descripción pendiente...")

                if proyecto["estado"].lower() == "finalizado":
                    st.success("✅ Finalizado")
                else:
                    st.warning("🛠️ En curso")

                if proyecto["repositorio"]:
                    st.markdown(f"[🔗 Repositorio]({proyecto['repositorio']})")

                if st.button(f"Ver más de {proyecto['titulo']}"):
                    st.session_state["proyecto_actual"] = proyecto
                    st.rerun()

            st.markdown("---")

    # Vista detallada
    else:
        proyecto = st.session_state["proyecto_actual"]
        st.header(f"📑 {proyecto['titulo']}")
        st.markdown(proyecto["detalle"])

        if st.button("⬅️ Volver a proyectos"):
            st.session_state["proyecto_actual"] = None
            st.rerun()
