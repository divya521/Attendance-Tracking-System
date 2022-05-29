import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import os
import cv2
import io
import base64

class FaceRec:
    
    def __init__(self, known_person_path_file, unknown_images_path_file):
        self.known_person_path_file = known_person_path_file
        self.unknown_images_path_file = unknown_images_path_file
         
    def converted_known_image(self,img_path):
        img = face_recognition.load_image_file(img_path)
        # img = cv2.resize(img, (400, 600), cv2.INTER_NEAREST)
        # img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return img

    def recognize_faces(self):
        stranger = self.converted_known_image(os.path.join(self.unknown_images_path_file, 'stranger.jpeg'))
        # cv2.imshow('stranger', stranger)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        match_name = '' 
        match_score = float('inf')
        stface_locations = face_recognition.face_locations(stranger)
        stface_encoding = face_recognition.face_encodings(stranger, stface_locations)
    
        for file in os.listdir(self.known_person_path_file):
            img_path = os.path.join(self.known_person_path_file, file)
            known_image = self.converted_known_image(img_path)
            # cv2.imshow('known_image', known_image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            known_image_locations = face_recognition.face_locations(known_image)
            known_image_encoding = face_recognition.face_encodings(known_image, known_image_locations)
            face_distance = face_recognition.face_distance(known_image_encoding, stface_encoding[0])
            # print(face_distance, img_path)
            if face_distance.size > 0:
                if face_distance[0] < match_score:
                    match_score = face_distance[0]
                    if file[-3:] == 'jpg':
                        match_name = file[:-4]
                    elif file[-3:] == 'png':
                        match_name = file[:-4]
                    else:
                        match_name = file[:-5]
        
        if match_score > 0.5:
            match_name = "nobody"
        return match_name
            
        


rec = FaceRec('./known-people' , './stranger')
# print(rec.recognize_faces())
