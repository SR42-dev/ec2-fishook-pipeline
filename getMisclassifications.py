# a script to update the misclassifications directory with the latest misclassifications on firebase
# download not working at the moment

# import libraries
import os
import firebase
from firebase_admin import credentials, initialize_app, storage

config = {
    "apiKey": "AIzaSyC8_9Jcl4qtkSTRwBc1i7p94S9SySo3ssM",
    "authDomain": "sih-clapforkrishna-c1752.firebaseapp.com",
    "databaseURL": "https://sih-clapforkrishna-c1752.firebaseio.com",
    "projectId": "sih-clapforkrishna-c1752",
    "storageBucket": "sih-clapforkrishna-c1752.appspot.com",
    "messagingSenderId": "1080893081827",
    "appId": "1:1080893081827:web:b46b25d435b414d236ddd6",
    "measurementId": "G-017J80KCYW",
    "serviceAccount": "./credentials/firebase-private-key.json"
}

cred = credentials.Certificate("./credentials/firebase-private-key.json")
initialize_app(cred, {'storageBucket': 'sih-clapforkrishna-c1752.appspot.com'})

bucket = storage.bucket()
localPath = 'misclassifications'

all_blob = bucket.list_blobs()

filePaths = []
for file in all_blob:
    if file.name[:18] == 'misclassifications':
        filePaths.append(file.name)

filePaths.pop(0)
print(filePaths)

for path in filePaths:
    blob = bucket.blob(path)
    blob.download_to_filename(path)
    

