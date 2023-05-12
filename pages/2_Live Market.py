import firebase_db as fdb
import streamlit as st
from layout import container

#import test

#st.set_page_config(page_title="Lve Market Page", page_icon="📈")
st.write(
    """testing through custom page in multiple pages """
)

# get user data for user with ID 123

#user_data = fdb.get_collection("May 2023")
user_data = fdb.get_collection("April 2023")

availabe_Trading_Dates = []  # create an empty list

# do something with the user data...
#st.write("user_data",user_data)
for doc in user_data:
    #st.write(doc.id, doc.to_dict())
    #st.json( doc.to_dict() )
    #st.write(doc.id)
    availabe_Trading_Dates.append(doc.id)
    


option = st.selectbox(
    'Select Trading Date',
    (availabe_Trading_Dates))

st.write('You selected:', option)


with container:
    st.selectbox("Select Trading Date", available_trading_dates)
