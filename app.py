import streamlit as st
import os
from google import genai

# Configuración básica
st.set_page_config(page_title="Tutor de Inglés IA", page_icon="🇬🇧")
st.title("🇬🇧 Tutor de Pronunciación IA")

# Inicialización segura del cliente
api_key = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY"))

if not api_key:
    st.error("❌ Faltando 'GEMINI_API_KEY' en los Secrets.")
    st.stop()

# Inicializamos el cliente. 
# Si el error 404 persiste, intentaremos una configuración explícita.
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"❌ Error al inicializar el cliente: {e}")
    st.stop()

user_input = st.text_area("Escribe tu frase en español:")

if st.button("Traducir y Analizar"):
    if user_input:
        with st.spinner("Consultando al tutor..."):
            try:
                # Usamos el modelo estable 'gemini-1.5-flash'
                # La estructura 'client.models.generate_content' es la correcta para el SDK google-genai
                response = client.models.generate_content(
                    model='gemini-1.5-flash',
                    contents=f"Eres un tutor de inglés. Traduce: {user_input}. Incluye fonética."
                )
                st.success(response.text)
            except Exception as e:
                st.error(f"Error técnico: {e}")
                st.info("Si el error persiste, intenta cambiando el modelo a 'gemini-1.5-pro'.")
