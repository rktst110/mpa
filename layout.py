import streamlit as st

container = st.beta_container()

with container:
    # elements to display in the container
    st.header("Container")
    st.write("This is a container")
