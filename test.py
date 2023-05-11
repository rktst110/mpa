# some other page in your web application
import streamlit as st

#from firebase import get_user_data
import firebase_db as fdb

# get user data for user with ID 123

user_data = fdb.get_collection("May 2023")

# do something with the user data...
st.write("user_data",user_data)
for doc in user_data:
    st.write(doc.id, doc.to_dict())
