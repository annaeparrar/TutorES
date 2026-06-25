import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="Tutor de Inglés IA", page_icon="🇬🇧")
st.title("🇬🇧 Traductor y Tutor de Pronunciación")

# Configuración de la API
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # USAR 'gemini-1.5-flash' SIN prefijos complejos
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Error de configuración: {e}")
    st.stop()

# Instrucciones
system_prompt = (
    "Eres un tutor de inglés. Responde exclusivamente con: "
    "\n1. Frase en Inglés: [Traducción]"
    "\n2. Pronunciación: [Fonética intuitiva en español. Si es necesario, añade IPA entre paréntesis]."
)

user_input = st.text_area("Escribe aquí tu frase en español:")

if st.button("Traducir"):
    if user_input:
        try:
            response = model.generate_content(f"{system_prompt}\n{user_input}")
            st.markdown("### Resultado:")
            st.success(response.text)
        except Exception as e:
            st.error(f"Error técnico: {e}")
