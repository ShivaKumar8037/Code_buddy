import streamlit as st
from palm_api import palmAPI




def documentationFunction(exampleCode, api_key):
    st.write("Documentation: ")
    documentation = palmAPI(api_key, f"Get the documentation of this code in the markdown format and follow best practices: {exampleCode}")

    if documentation:
        # Display the documentation
        st.markdown(documentation)

        # Create a download button for the documentation in Markdown format
        st.download_button(
            label="Download Documentation as Markdown",
            data=documentation,
            file_name="documentation.md",
            mime="text/markdown"
        )

    return documentation



def show(api_key=None):
    st.title("Documentation")
    if api_key: 
        if 'example_code' in st.session_state:
            # Access the exampleCode
            exampleCode = st.session_state['example_code']
            
            # Display or process the exampleCode
            st.code(exampleCode)
            documentationFunction(exampleCode, api_key)
        else:
            st.write("No example code was provided in code Expaliner Page.")
    else: 
        st.warning("Please enter your API key in the sidebar to access this feature.")