# Proyecto de Preguntas a IA sobre Video de YouTube con Interfaz en Streamlit

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar una interfaz de usuario utilizando Streamlit para interactuar con una inteligencia artificial (IA) capaz de responder preguntas relacionadas con un video de YouTube. La IA será entrenada para comprender el contenido del video y proporcionar respuestas precisas a las preguntas formuladas por el usuario.

## Tecnologías Utilizadas

- **Streamlit:** Una biblioteca de Python para la creación de aplicaciones web interactivas con facilidad.

- **YouTube API:** Se utilizará la API de YouTube para obtener información sobre el video.

- **Procesamiento del Lenguaje Natural (NLP):** Modelo gpt-3.5 utilizado a travez de la api de openAI
## Estructura del Proyecto

El proyecto se dividirá en los siguientes componentes principales:

1. **Interfaz de Usuario con Streamlit:**
   - Pantalla principal que permite al usuario ingresar la URL del video de YouTube.
   - Sección para introducir preguntas que se realizarán a la IA.

2. **Integración con YouTube API:**
   - Extracción de información del video utilizando la API de YouTube.

3. **Modelo de Preguntas y Respuestas (Q&A):**
   - Implementación del a travez de la api
   - Generación de respuestas basadas en el análisis del contenido del video.

4. **Despliegue:**
   - Configuración de un entorno de producción para la aplicación Streamlit.
   - Implementación de la interfaz y la lógica de la IA en un servidor web accesible.

## Ejecución del Proyecto

Asegúrate de tener las bibliotecas necesarias instaladas. Puedes hacerlo ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
