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

KEY_Val = os.environ['FACE_SUBSCRIPTION_KEY']
ENDPOINT_Val = os.environ['FACE_ENDPOINT']
