import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType

#KEY = 'bb170de71ae24dfa8f17d2a472215bfe' # os.environ['FACE_SUBSCRIPTION_KEY']
#ENDPOINT = 'https://cloud-project-face-service.cognitiveservices.azure.com/' # os.environ['FACE_ENDPOINT']
#
#face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
#
## Detect a face in an image that contains a single face
#single_face_image_url = 'https://www.biography.com/.image/t_share/MTQ1MzAyNzYzOTgxNTE0NTEz/john-f-kennedy---mini-biography.jpg'
#single_image_name = os.path.basename(single_face_image_url)
#detected_faces = face_client.face.detect_with_url(url=single_face_image_url)
#if not detected_faces:
#    raise Exception('No face detected from image {}'.format(single_image_name))
#
## Display the detected face ID in the first single-face image.
## Face IDs are used for comparison to faces (their IDs) detected in other images.
#print('Detected face ID from', single_image_name, ':')
#for face in detected_faces: print (face.face_id)
#print()
#
## Save this ID for use in Find Similar
#first_image_face_ID = detected_faces[0].face_id
