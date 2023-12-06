import streamlit as st
import codeExplainer, vulnerabilityAssessment, documentation, testCases, codeTranslation, home
from palm_api import palmAPI  

pages = {
    "Home": home,
    "Code Explainer": codeExplainer,
    "Security Vulnerability Assessment": vulnerabilityAssessment,
    "Documentation": documentation,
    "Test Cases": testCases,
    'Translate your code': codeTranslation,
    # Add more pages here
}

def main():
    st.sidebar.title("Code Buddy Services")
    user_api_key = st.sidebar.text_input("Enter your API key ", type="password", key="user_api_key_input")

    if user_api_key:
        st.sidebar.success("API Key entered successfully!")
    
    # Allow the user to select a page
    page = st.sidebar.radio("Navigate", tuple(pages.keys()))

    # If an API key is required for the selected page, pass it; otherwise, call without the API key
    if page != "Home" and user_api_key:
        pages[page].show(user_api_key)
    else:
        pages[page].show()

if __name__ == "__main__":
    main()
