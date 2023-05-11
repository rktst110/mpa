# firebase.py module

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# initialize Firebase app with your project credentials
cred = credentials.Certificate('/path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-name.firebaseio.com/'
})

# create a reference to the Firebase Realtime Database
ref = db.reference()

# define a method to retrieve user data from Firebase
def get_user_data(user_id):
    user_ref = ref.child('users').child(user_id)
    user_data = user_ref.get()
    return user_data
