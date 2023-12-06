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

    st.markdown("---")
    st.subheader("About the Creator")
    st.markdown("""
    Code Buddy was conceptualized and developed by [Shiva Kumar](https://github.com/ShivaKumar8037), aimed at providing an intuitive and efficient coding experience. With a passion for enhancing developer tools and workflows, [Your Name] has integrated cutting-edge AI technologies to bring Code Buddy to life. Check out the project on [GitHub](https://github.com/yourgithubusername/code-buddy) for more details, contributions, and updates.
    """)

    # Instructions or additional information (if needed)
    st.info("Enter your API key in the sidebar to access all features.")
