from langchain.llms import OpenAI


def agente_res(texto,api,prompt):
    text = texto
    llm = OpenAI(temperature=0,openai_api_key = api,)
    prompt = f"""{prompt}, esto sacalo del siguiente texto: {text}"""
    respuesta = llm(prompt)
    return respuesta

def resumidor(texto,api,prom):
    text = texto
    llm = OpenAI(temperature=0,openai_api_key = api,)
    prompt = f"""dame una respuesta general con el siguiente texto: {texto}
de la siguinte pregunta {prom}

"""
    respuesta = llm(prompt)
    return respuesta