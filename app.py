import streamlit as st
from import_transc_yt import transcript_url
import math
from agentes import agente_res, resumidor
import time


# Streamlit Configuration
st.title("Get YouTube Video Summary")
url = st.text_input("Enter YouTube URL:")
api_key = st.text_input("Enter your API key. You can get one at https://platform.openai.com/api-keys:")
prompt = st.text_input("What information are you looking for in the video?")

def achicar(texto,pasadas,promp):
    if len(texto) >= 4096:
        cantidad = math.ceil(len(texto)/4096)
    
    lista = {}
    for i in range(0,cantidad):
        lista[f"texto{i}"] = texto[(i*4096):(4096*(1+i))]
    
    respuestas = {}
    for i in range(0, cantidad):
        respuestas[f"respuesta{i}"] = agente_res(lista[f"texto{i}"], api_key,promp)
        
        # Check if a batch of three iterations has been completed
        if (pasadas + 1) % 3 == 0:
            print("Pausing for 60 seconds...")
            time.sleep(60)
            print("60 seconds have elapsed")
        
        pasadas += 1

    resumen = ""
    for i in range(0, cantidad):
        resumen += respuestas[f"respuesta{i}"]
        
    return resumen,pasadas

button_pressed = st.button("Get Summary")

# Check if the button was pressed
if button_pressed:
    # Verify user input
    try:
        if not url or not api_key or not prompt:
            st.warning("Please fill out all fields.")
        else:
            # Get YouTube video transcript
            st.info("Processing video...")
            video_transcript = transcript_url(url)

            # Process transcript in batches
            passes = 0
            while True:
                # Get summary and update pass counter
                summary, passes = achicar(video_transcript, passes, prompt)
                # Check summary length
                if len(summary) < 4096:
                    break
                else:
                    st.warning("El resumen es mayor a los tokens necesarios, se procesará nuevamente.")

            # Pausar si es necesario
            if (passes + 1) % 3 == 0:
                st.info("wait 60s...")
                time.sleep(60)
                st.info("End of 60 s")

            # Obtener resumen final
            final_summary = resumidor(summary, api_key, prompt)
            st.success("I finish the summary")
            st.subheader("Answer:")
            st.write(final_summary)
    except Exception as e:
        st.write(f"The process could not be completed due to the following error: {e}")