import streamlit as st
from palm_api import palmAPI



def show(api_key = None):
    st.title("Code Translation")

    if api_key:
        if 'example_code' in st.session_state:
            exampleCode = st.session_state['example_code']
            
            st.subheader("Your Original Code (Source Language)")
            st.code(exampleCode)

            lang = st.text_input("Enter the target language you want to translate to", 'Java')
            st.subheader("Translated Code (Target Language)")
            translated_code = translate_code_to_target_language(exampleCode, lang, api_key)
            st.code(translated_code)
        else:
            st.write("No example code was provided in the code Explainer page.")
    else:
        st.warning("Please enter your API key in the sidebar to access this feature.")

def translate_code_to_target_language(exampleCode, lang, api_key):
    translated_code = palmAPI(api_key, f"Translate this code {exampleCode} to {lang} Language.")
    return translated_code

