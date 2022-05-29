from flask import Flask, request, request_started
from flask_cors import CORS
import json
from face_rec import FaceRec, rec
from PIL import Image
import base64
import io
import os
import shutil
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
from firebase_db import updpresent

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')
 
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://face-recognition-d754f-default-rtdb.firebaseio.com/'
})


app = Flask(__name__)
CORS(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    directory = './known-people'
    if data:
        known_name = data['name']
        result = data['data']
        
        b = bytes(result, 'utf-8')
        image = b[b.find(b'/9'):]
        im = Image.open(io.BytesIO(base64.b64decode(image)))
        im.save(directory+'/'+known_name+'.jpeg')
        return "Successfully Registered!"
    else:
        return "Registration Unsuccessful"

@app.route('/api', methods=['POST', 'GET'])
def api():
	data = request.get_json()
	resp = 'Nobody'
	directory = './stranger'
	if data:
		if not os.path.exists(directory):
			# try:
			os.mkdir(directory)
			print("Directory created!")
			time.sleep(1)
   
		result = data['data']
		b = bytes(result, 'utf-8')
		image = b[b.find(b'/9'):]
		im = Image.open(io.BytesIO(base64.b64decode(image)))
		im.save(directory+'/stranger.jpeg')

		resp = rec.recognize_faces()
		print(resp)
		if resp == "nobody":
			if data['status'] == 'login':
				return "Login Unsuccessful"
			else:
				return "Logout Unsuccessful"
		else:
			updpresent(resp, data['status'])
			if data['status'] == 'login':
				return "Logged in Successfully"
			else:
				return "Logged out Successfully"

			# except:
			# 	pass
	
	return "No data recieved"


	







if __name__ == '_main_':
	app.run()