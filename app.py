import streamlit as st
import google.generativeai as genai

# Configuración de la página web
st.set_page_config(page_title="Tutor de Inglés IA", page_icon="🇬🇧")

# Título y encabezado
st.title("🇬🇧 Traductor y Tutor de Pronunciación")
st.markdown("Escribe una frase en español y obtén su traducción y guía fonética.")

# Configuración de la API Key desde los Secrets de Streamlit
try:
    # Asegúrate de que el nombre aquí coincida con lo que pusiste en Streamlit Cloud
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("Error: La API Key no está configurada correctamente en los Secrets.")
    st.stop()

# Configuración del modelo
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Instrucción de sistema (System Prompt)
system_prompt = (
    "Eres un tutor de inglés experto. Tu única función es recibir frases en español "
    "y devolver una respuesta estricta con este formato: "
    "\n\n1. Frase en Inglés: [Traducción natural al inglés] "
    "\n2. Pronunciación: [Transcripción fonética para un hispanohablante] "
    "\n\nNo escribas saludos, explicaciones gramaticales ni nada adicional."
)

# Interfaz de usuario
user_input = st.text_area("Escribe aquí tu frase en español:")

if st.button("Traducir"):
    if user_input:
        with st.spinner('Consultando a Gemini...'):
            try:
                # Construimos el prompt completo con la instrucción
                full_prompt = f"{system_prompt}\n\nFrase a traducir: {user_input}"
                response = model.generate_content(full_prompt)
                
                # Mostrar resultados
                st.markdown("---")
                st.markdown("### Resultado:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Ocurrió un error al procesar la solicitud: {e}")
    else:
        st.warning("Por favor, ingresa una frase antes de hacer clic en traducir.")
