import firebase_db as fdb
import streamlit as st
from layout import container

#st.set_page_config(page_title="Live Market Page", page_icon="📈")
st.write("Testing through custom page in multiple pages")

# Get user data for user with ID 123
user_data = fdb.get_collection("April 2023")

# Create a list of available trading dates
available_trading_dates = [doc.id for doc in user_data]

# Display a select box with the available trading dates
with container:
    st.selectbox("Select Trading Date", available_trading_dates)
