import streamlit as st
from palm_api import palmAPI

def show(api_key=None):
    st.title("Automated Test Case Generator")

    
    if api_key:
        if 'example_code' in st.session_state:
            exampleCode = st.session_state['example_code']
            
            st.subheader("Your Code")
            st.code(exampleCode)

            st.subheader("Generated Test Cases")
            test_cases = palmAPI(api_key, f"Generate test cases for this Python code: \n\n{exampleCode}")
            st.text_area("Test Cases", test_cases, height=200)

            st.subheader("Suggested Edge Cases")
            edge_cases = palmAPI(api_key, f"Generate edge cases for this Python code: \n\n{exampleCode}")
            st.text_area("Edge Cases", edge_cases, height=200)
        else:
            st.write("No example code was provided in the code Explainer page.")
    else:
        st.warning("Please enter your API key in the sidebar to access this feature.")
