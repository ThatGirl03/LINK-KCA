import json
import os
from dotenv import load_dotenv
from firebase_admin import credentials, firestore, initialize_app

load_dotenv()

# Get the path to the Firebase key JSON file from the environment variable
firebase_key_path = os.getenv('FIREBASE_KEY_PATH')

if not firebase_key_path:
    raise Exception("FIREBASE_KEY_PATH environment variable is not set.")

# Load the Firebase key JSON file into a dictionary
with open(firebase_key_path) as f:
    firebase_key_dict = json.load(f)

# Initialize Firebase using the Firebase Admin SDK private key JSON dictionary
cred = credentials.Certificate(firebase_key_dict)
initialize_app(cred)

# Set up Firestore client
db = firestore.client()
