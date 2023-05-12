import streamlit as st
import inspect
import textwrap
import time
import numpy as np
from utils import show_code

import firebase_db as fdb
#import test

st.set_page_config(page_title="firestore testing", page_icon="📈")
st.write(
    """testing through custom page in multiple pages """
)

# get user data for user with ID 123
user_data = fdb.get_collection("May 2023")

# do something with the user data...
st.write("user_data",user_data)
for doc in user_data:
    #st.write(doc.id, doc.to_dict())
    st.write(doc.id)
    #st.json( doc.to_dict() )




option = st.selectbox(
    'How would you like to be contacted?',
    (Object.keys(user_data)))

st.write('You selected:', option)