import streamlit as st
import requests

from conocimiento import HISTORIA, PERSONAJES, obtener_conocimiento

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2:latest"

def preguntar_ia(prompt):

    respuesta = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    if respuesta.status_code == 200:
        return respuesta.json()["response"]

    return "Ocurrió un error al comunicarse con Ollama."

# ==========================================
# CONFIGURACIÓN
# ==========================================

st.set_page_config(
    page_title="JoJo's Bizarre Adventure",
    page_icon="⭐",
    layout="wide"
)


# ==========================================
# MENÚ LATERAL
# ==========================================

st.sidebar.title("⭐ JoJo's Bizarre Adventure")

st.sidebar.write(
    "Portal interactivo sobre la historia y personajes."
)

pagina = st.sidebar.radio(
    "Navegación",
    [
        "🏠 Inicio",
        "📖 Historia",
        "👤 Personajes",
        "📝 Resumen IA",
        "💬 Pregúntale a la IA"
    ]
)


# ==========================================
# INICIO
# ==========================================

if pagina == "🏠 Inicio":

    st.title("⭐ JoJo's Bizarre Adventure")

    st.subheader(
        "Portal interactivo de información"
    )

    st.write(
        """
        Bienvenido al portal de información sobre
        **JoJo's Bizarre Adventure**.

        En este sitio podrás consultar información sobre
        la historia y diferentes personajes de la serie.

        También podrás utilizar inteligencia artificial
        para generar resúmenes y responder preguntas.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Partes",
            "6"
        )

    with col2:
        st.metric(
            "Personajes",
            len(PERSONAJES)
        )

    with col3:
        st.metric(
            "IA",
            "Ollama"
        )


# ==========================================
# HISTORIA
# ==========================================

elif pagina == "📖 Historia":

    st.title("📖 Historia")

    st.write(HISTORIA)


# ==========================================
# PERSONAJES
# ==========================================

elif pagina == "👤 Personajes":

    st.title("👤 Personajes")

    personaje = st.selectbox(
        "Selecciona un personaje",
        list(PERSONAJES.keys())
    )

    datos = PERSONAJES[personaje]

    st.header(personaje)

    st.write(
        f"**Parte:** {datos['parte']}"
    )

    st.write(
        datos["descripcion"]
    )


# ==========================================
# RESUMEN IA
# ==========================================

elif pagina == "📝 Resumen IA":

    st.title("📝 Resumen con Inteligencia Artificial")

    st.write(
        """
        La inteligencia artificial analizará la información
        disponible en este portal y generará un resumen.
        """
    )

    if st.button("🤖 Generar resumen"):

        conocimiento = obtener_conocimiento()

        prompt = f"""
Eres un asistente especializado en JoJo's Bizarre Adventure.

Utiliza únicamente la información proporcionada a continuación.

INFORMACIÓN DEL PORTAL:
{conocimiento}

TAREA:
Realiza un resumen claro y ordenado de la información.
Incluye las principales partes de la historia y los personajes
más importantes mencionados.

No inventes información que no aparezca en el contenido.

RESUMEN:
"""

        with st.spinner("La IA está generando el resumen..."):

            resumen = preguntar_ia(prompt)

        st.subheader("📋 Resumen")

        st.write(resumen)


# ==========================================
# PREGUNTAS IA
# ==========================================

elif pagina == "💬 Pregúntale a la IA":

    st.title("💬 Pregúntale a la IA")

    st.write(
        """
        Haz una pregunta sobre la historia o los personajes
        que aparecen en este portal.
        """
    )

    pregunta = st.text_input(
        "Escribe tu pregunta",
        placeholder="¿Quién es Jotaro Kujo?"
    )

    if st.button("🤖 Preguntar"):

        if pregunta:

            conocimiento = obtener_conocimiento()

            prompt = f"""
Eres un asistente que responde preguntas sobre
JoJo's Bizarre Adventure.

Debes utilizar ÚNICAMENTE la información proporcionada
en la base de conocimiento.

Si la respuesta no se encuentra en la información,
responde:

"No tengo suficiente información en la base de conocimiento."

No inventes información.

BASE DE CONOCIMIENTO:
{conocimiento}

PREGUNTA DEL USUARIO:
{pregunta}

RESPUESTA:
"""

            with st.spinner("La IA está pensando..."):

                respuesta = preguntar_ia(prompt)

            st.subheader("🤖 Respuesta")

            st.write(respuesta)

        else:

            st.warning("Escribe una pregunta.")