import os, requests, uuid, json

def getTranslatedText():
  subscription_key = '2a9eaaaee36b45c58c09b79d317e0b72'
  endpoint = 'https://cloud-project-translate-service.cognitiveservices.azure.com/sts/v1.0/issuetoken'
  path = '/translate?api-version=3.0'
  params = '&to=de&to=it'
  constructed_url = endpoint + path + params
  
  headers = {
      'Ocp-Apim-Subscription-Key': subscription_key,
      'Content-type': 'application/json',
      'X-ClientTraceId': str(uuid.uuid4())
  }
  
  body = [{
      'text': 'Hello World!'
  }]
  
  request = requests.post(constructed_url, headers=headers, json=body)
  response = request.json()
  
  return json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))