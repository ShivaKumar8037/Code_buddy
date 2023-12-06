import google.generativeai as palm
from llama_index.llms.palm import PaLM

def palmAPI(api_key, prompt):
    palm.configure(api_key=api_key)
    model = PaLM(api_key=api_key)
    return model.complete(prompt).text
