import json
import os
from dotenv import load_dotenv
from firebase_admin import credentials, firestore, initialize_app

load_dotenv()
# Get Firebase key from environment variable
firebase_key_json = os.getenv('FIREBASE_KEY')

if not firebase_key_json:
    raise Exception("FIREBASE_KEY environment variable is not set.")

# Parse the Firebase key JSON string to a Python dictionary
firebase_key_dict = json.loads(firebase_key_json)

# Initialize Firebase using the Firebase Admin SDK private key JSON dictionary
cred = credentials.Certificate(firebase_key_dict)
initialize_app(cred)

# Set up Firestore client
db = firestore.client()
