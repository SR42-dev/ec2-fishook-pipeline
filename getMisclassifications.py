# a script to update the misclassifications directory with the latest misclassifications on firebase

# import libraries
import pyrebase

'''
config = {
    api_key=,
    authDomain=,
    databaseURL=,
    projectId=,
    storageBucket=,
    messagingSenderId=,
    appId=,
    measuremtnId=
}
'''

config = {
  "project_info": {
    "project_number": "1080893081827",
    "project_id": "sih-clapforkrishna-c1752",
    "storage_bucket": "sih-clapforkrishna-c1752.appspot.com"
  },
  "client": [
    {
      "client_info": {
        "mobilesdk_app_id": "1:1080893081827:android:0ae3236b9783029336ddd6",
        "android_client_info": {
          "package_name": "com.DragonDare.sih_fishook"
        }
      },
      "oauth_client": [
        {
          "client_id": "1080893081827-24irmgb26m33faqi1js2m3r46v2bki7k.apps.googleusercontent.com",
          "client_type": 1,
          "android_info": {
            "package_name": "com.DragonDare.sih_fishook",
            "certificate_hash": "fe8c2353da58e30d7bdacd25114cb007e464853a"
          }
        },
        {
          "client_id": "1080893081827-4st64vq34fdtm1rjarj0rresm0c6feod.apps.googleusercontent.com",
          "client_type": 3
        }
      ],
      "api_key": [
        {
          "current_key": "AIzaSyCM-BDFMhzapZHGXWZ42__eSERXg1ls0TM"
        }
      ],
      "services": {
        "appinvite_service": {
          "other_platform_oauth_client": [
            {
              "client_id": "1080893081827-4st64vq34fdtm1rjarj0rresm0c6feod.apps.googleusercontent.com",
              "client_type": 3
            },
            {
              "client_id": "1080893081827-drob1mk692r2oii20c00ul927e64f8p7.apps.googleusercontent.com",
              "client_type": 2,
              "ios_info": {
                "bundle_id": "com.DragonDare.sihFishook"
              }
            }
          ]
        }
      }
    }
  ],
  "configuration_version": "1"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


 

