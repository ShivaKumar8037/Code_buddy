import streamlit as st

def show():
    st.header('Welcome to Code Buddy 🚀')

    st.write('Code Buddy is a tool designed to assist you in writing better code. '
             'It offers a variety of features to enhance your coding experience. '
             'Explore the services we offer to make your coding journey smoother and more efficient.')

    # Using markdown for a better layout
    st.markdown("""
    ### Features of Code Buddy
    * **Code Explainer**: Understand complex code snippets with ease.
    * **Security Vulnerability Assessment**: Evaluate your code for potential security threats.
    * **Documentation**: Generate comprehensive documentation for your code.
    * **Test Cases**: Automatically create test cases for your software.
    * **Translate Your Code**: Translate code between different programming languages.

    ### Getting Started
    Select a service from the sidebar to begin exploring Code Buddy's features. Each service is tailored to improve specific aspects of your coding workflow.

    ### Obtaining an API Key from Palm
    To access all the features of Code Buddy, you will need an API key from Palm. Follow these steps to get your API key:
    1. Visit the [Palm API Setup Page](https://developers.generativeai.google/tutorials/setup).
    2. Follow the instructions to register and create an API key.
    3. Once you have your API key, enter it in the sidebar of this app.

    Remember, keep your API key secure and do not share it publicly.
    """)

    

    # Instructions or additional information (if needed)
    st.info("Enter your API key in the sidebar to access all features.")

    #testing

    
