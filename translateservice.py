import os, requests, uuid, json

def getTranslatedText(initial_text, target_language):
  subscription_key = '2a9eaaaee36b45c58c09b79d317e0b72'
  endpoint = 'https://api.cognitive.microsofttranslator.com'
  path = '/translate?api-version=3.0'
  params = '&to=it'
  constructed_url = endpoint + path + params
  
  headers = {
      'Ocp-Apim-Subscription-Key': subscription_key,
      'Content-type': 'application/json',
      'X-ClientTraceId': str(uuid.uuid4())
  }
  
  body = [{
      'text': 'hello'
  }]
  
  request = requests.post(constructed_url, headers=headers, json=body)
  response = request.json()
  
  return json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))
