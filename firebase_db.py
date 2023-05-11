# firebase.py module

from google.cloud import firestore


# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("nse-data-saving-2023-5hf5fgdrg-firebase-adminsdk-yzdk6-d335b442d8.json")


#doc_ref = db.collection("April 2023").document("13 April 2023")
#docs = db.collection("Test").document("DocTest")

"""
docs = db.collection('Test').stream()
#st.write(docs)
for doc in docs:
    st.write(doc.id, doc.to_dict())
"""

def get_collection(collection_name):
    coll = db.collection(collection_name).stream()
    return coll


# define a method to retrieve user data from Firebase
def get_user_data(user_id):
    user_ref = ref.child('users').child(user_id)
    user_data = user_ref.get()
    return user_data

