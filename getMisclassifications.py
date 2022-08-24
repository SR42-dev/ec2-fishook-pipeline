# a script to update the misclassifications directory with the latest misclassifications on firebase

# import libraries
import pyrebase

config = {
    'api_key':'AIzaSyCM-BDFMhzapZHGXWZ42__eSERXg1ls0TM',
    'authDomain':'sih-clapforkrishna-c1752.firebaseapp.com',
    'databaseURL':'https://sih-clapforkrishna-c1752.firebaseio.com',
    'projectId':'sih-clapforkrishna-c1752',
    'storageBucket':'sih-clapforkrishna-c1752.appspot.com',
    'messagingSenderId':'1080893081827',
    'appId':'1:1080893081827:android:0ae3236b9783029336ddd6',
    'measurementId':''
}


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


 

