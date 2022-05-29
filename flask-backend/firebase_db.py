import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
 
 
# # Fetch the service account key JSON file contents
# cred = credentials.Certificate('serviceAccountKey.json')
 
# # Initialize the app with a service account, granting admin privileges
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://face-recognition-d754f-default-rtdb.firebaseio.com/'
# })



def updpresent(name, status):
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    timenow = now.strftime("%H:%M:%S")
    print("here")
    ref = db.reference('/students/').child(name).child(date).child(status)
    ref.set({'time': timenow})