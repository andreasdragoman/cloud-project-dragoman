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

KEY =  os.environ['FACE_SUBSCRIPTION_KEY'] # 'bb170de71ae24dfa8f17d2a472215bfe'
ENDPOINT = os.environ['FACE_ENDPOINT'] # 'https://cloud-project-face-service.cognitiveservices.azure.com/'

def getFacesInfoFromURL():
  global KEY
  global ENDPOINT
  # face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
  return KEY
