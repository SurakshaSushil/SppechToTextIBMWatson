import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def convert(file):
    authenticator = IAMAuthenticator('rdYD6AzTRCobsj-VeGo1SsgBtXJQNTEJCmBy7SrlIZAk')
    service = SpeechToTextV1(authenticator=authenticator)
    service.set_service_url('https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/b565a925-d534-415f-b88d-6b214c8b2ea1')
    with open(join(dirname('__file__'), file),
              'rb') as audio_file:
        dic = json.dumps(
            service.recognize(
                audio=audio_file,
                content_type='audio/wav',
                timestamps=True,
            continuous=True, indent=2).get_result())
    y = json.loads(dic)
    for i in y['results']:
        for j in i['alternatives']:
            for k in j['timestamps']:
                print(k)
    str = " "
    str = y.get('results').pop().get('alternatives').pop().get('transcript') + str[:]
    return str