import streamlit as st
from import_transc_yt import transcript_url
import math
from agentes import agente_res, resumidor
import time


# Configuración de Streamlit
st.title("Obtener Resumen de Video de YouTube")
url = st.text_input("Ingrese la URL de YouTube:")
api_key = st.text_input("Ingrese su clave de API:")
prompt = st.text_input("¿Que informacion busca en el video?")

def achicar(texto,pasadas,promp):
    if len(texto) >= 4096:
        cantidad = math.ceil(len(texto)/4096)
    
    lista = {}
    for i in range(0,cantidad):
        lista[f"texto{i}"] = texto[(i*4096):(4096*(1+i))]
    
    respuestas = {}
    for i in range(0, cantidad):
        respuestas[f"respuesta{i}"] = agente_res(lista[f"texto{i}"], api_key,promp)
        
        # Verificar si se ha completado un lote de tres iteraciones
        if (pasadas + 1) % 3 == 0:
            print("Pausando durante 60 segundos...")
            time.sleep(60)
            print("Finalizaron los 60 segundos")
        
        pasadas += 1

    resumen = ""
    for i in range(0, cantidad):
        resumen += respuestas[f"respuesta{i}"]
        
    return resumen,pasadas

button_pressed = st.button("Obtener Resumen")

# Verificar si se presionó el botón
if button_pressed:
    # Verificar la entrada del usuario
    try:
        if not url or not api_key or not prompt:
            st.warning("Por favor, complete todos los campos.")
        else:
            # Obtener transcripción del video de YouTube
            st.info("Procesando el video...")
            video_transcript = transcript_url(url)

            # Procesar la transcripción en lotes
            passes = 0
            while True:
                # Obtener resumen y actualizar el contador de pasadas
                summary, passes = achicar(video_transcript, passes, prompt)
                # Verificar la longitud del resumen
                if len(summary) < 4096:
                    break
                else:
                    st.warning("El resumen es mayor a los tokens necesarios, se procesará nuevamente.")

            # Pausar si es necesario
            if (passes + 1) % 3 == 0:
                st.info("Pausando durante 60 segundos...")
                time.sleep(60)
                st.info("Finalizaron los 60 segundos")

            # Obtener resumen final
            final_summary = resumidor(summary, api_key, prompt)
            st.success("Finalizo el resumen")
            st.subheader("Resumen Final:")
            st.write(final_summary)
    except Exception as e:
        st.write(f"No se pudo completar el proceso por el siguiente error: {e}")