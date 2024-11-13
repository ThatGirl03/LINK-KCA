import os
from dotenv import load_dotenv
from firebase_admin import credentials, firestore, initialize_app
from google.cloud import storage 

# Load environment variables from .env
load_dotenv()

# Construct the Firebase credentials dictionary from environment variables
firebase_key_dict = {
    "type": os.getenv("FIREBASE_TYPE"),
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN")
}

# Initialize Firebase using the credentials dictionary
cred = credentials.Certificate(firebase_key_dict)
initialize_app(cred, {
    'storageBucket': os.getenv("FIREBASE_STORAGE_BUCKET")  # Set the storage bucket
})
               
# Set up Firestore client
db = firestore.client()


# Set up Firebase Storage client
storage_client = storage.Client.from_service_account_info(firebase_key_dict)
bucket = storage_client.bucket(os.getenv("FIREBASE_STORAGE_BUCKET"))


def upload_file_to_firebase(file_path, destination_blob_name):
    """Uploads a file to Firebase Storage and returns the public URL."""
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(file_path)
    blob.make_public()
    print(f"File uploaded to {blob.public_url}")
    return blob.public_url