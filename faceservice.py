# import asyncio
# import io
# import glob
import os
# import sys
# import time
# import uuid
# import requests
# from urllib.parse import urlparse
# from io import BytesIO
# from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
# from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType

KEY = 'bb170de71ae24dfa8f17d2a472215bfe'
ENDPOINT = 'https://cloud-project-face-service.cognitiveservices.azure.com/'

def getFaceInfoFromURL():
  face_detected = False
  url = 'https://www.biography.com/.image/t_share/MTQ1MzAyNzYzOTgxNTE0NTEz/john-f-kennedy---mini-biography.jpg'
  face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
  single_face_image_url = url
  single_image_name = os.path.basename(single_face_image_url)
  detected_faces = face_client.face.detect_with_url(url=single_face_image_url)
  if not detected_faces:
    return 'NOPE'
  return detected_faces
