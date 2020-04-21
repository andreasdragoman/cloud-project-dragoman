import os
import requests
import json
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

KEY = 'bb170de71ae24dfa8f17d2a472215bfe'
ENDPOINT = 'https://cloud-project-face-service.cognitiveservices.azure.com/'

def getFaceInfoFromURL(urlImg):
  subscription_key = 'bb170de71ae24dfa8f17d2a472215bfe'
  # face_detected = False
  # url = 'https://www.biography.com/.image/t_share/MTQ1MzAyNzYzOTgxNTE0NTEz/john-f-kennedy---mini-biography.jpg'
  # face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
  # single_face_image_url = url
  # single_image_name = os.path.basename(single_face_image_url)
  # detected_faces = face_client.face.detect_with_url(url=single_face_image_url)
  # if not detected_faces:
  #   return None
  # return detected_faces
  # replace <My Endpoint String> with the string from your endpoint URL
  face_api_url = 'https://cloud-project-face-service.cognitiveservices.azure.com/face/v1.0/detect'
  
  image_url = urlImg # 'https://upload.wikimedia.org/wikipedia/commons/3/37/Dagestani_man_and_woman.jpg'
  
  headers = {'Ocp-Apim-Subscription-Key': subscription_key}
  
  params = {
      'returnFaceId': 'true',
      'returnFaceLandmarks': 'false',
      'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
  }
  
  response = requests.post(face_api_url, params=params,
                           headers=headers, json={"url": image_url})
  return response.json()
