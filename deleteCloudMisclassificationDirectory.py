# a script to udelete all records in the misclassifications directory

# import libraries
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

cloudPath = "misclassifications/"
localPath = "./misclassifications"

misclassifiedFiles = storage.child(cloudPath).list_files()
listOfMisclassifiedFiles = []
for file in misclassifiedFiles :
    if file.name.find('misclassifications') != -1 :
        listOfMisclassifiedFiles.append(file.name)

listOfMisclassifiedFiles.pop(0)

for file in listOfMisclassifiedFiles :
    print('Cloud path : ', cloudPath + file[19:])
    print('Local path : ', localPath + '/' + file[19:])
    storage.child(cloudPath + file[19:]).delete(cloudPath + file[19:])

    