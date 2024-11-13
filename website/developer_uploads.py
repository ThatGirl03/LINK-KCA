"""

from datetime import datetime
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# upload_videos.py
from firebase_config import upload_file_to_firebase, db

# Define local file path and Firebase Storage path
file_path = r"C:\Users\CC\Downloads\software.mp4"  # Replace with actual path
destination_blob_name = "videos/software.mp4"  # Specify desired path in Firebase Storage

# Upload the file and get the public URL
public_url = upload_file_to_firebase(file_path, destination_blob_name)

# Store the URL in Firestore
video_data = {
    "name": "Software Engineering Past Paper",  # Customizable
    "url": public_url,
    "timestamp": datetime.now()
}
db.collection('videos').add(video_data)

print("Uploaded file URL:", public_url)
"""