import firebase_db as fdb
import streamlit as st


container = st.container()

with container:
    # elements to display in the container
    st.header("Container")
    #st.set_page_config(page_title="Live Market Page", page_icon="📈")
    st.write("This is a container")
    


def on_trading_date_selected(new_value):
    # Do something with the new value of the selectbox
    st.write("Selected trading date:", new_value)


# Get user data for user with ID 123
user_data = fdb.get_collection("April 2023")

# Create a list of available trading dates
available_trading_dates = [doc.id for doc in user_data]

# Display a select box with the available trading dates
with container:
    selected_trading_date = st.selectbox("Select Trading Date", available_trading_dates)

# Call the `on_trading_date_selected()` function when the value of the selectbox changes
selected_trading_date.on_change(on_trading_date_selected)