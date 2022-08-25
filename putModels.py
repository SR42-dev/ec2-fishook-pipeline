# a script to update the misclassifications directory with the latest misclassifications on firebase

# import libraries
import os
import pyrebase

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

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

cloudPath = "model/"
localPath = "./model/" 

for file in os.listdir(localPath):
    storage.child(cloudPath + file).put(localPath + file)