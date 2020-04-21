import os
import requests
import json
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

KEY = 'bb170de71ae24dfa8f17d2a472215bfe'
ENDPOINT = 'https://cloud-project-face-service.cognitiveservices.azure.com/'

def getFaceInfoFromURL(urlImg):
  subscription_key = 'bb170de71ae24dfa8f17d2a472215bfe'
  face_api_url = 'https://cloud-project-face-service.cognitiveservices.azure.com/face/v1.0/detect'
  image_url = urlImg  
  headers = {'Ocp-Apim-Subscription-Key': subscription_key} 
  params = {
      'returnFaceId': 'true',
      'returnFaceLandmarks': 'false',
      'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
  }
  response = requests.post(face_api_url, params=params,
                           headers=headers, json={"url": image_url})
  return json.dumps(response.json())
