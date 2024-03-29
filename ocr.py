import requests
import uuid
import time
import json
from models import Images

SECRET_KEY = "d1ZGemRIU2V0bFNTd2lkSUFNeG9ualBGdWtaSXptQ1c="
OCR_URL = "https://83cp3mih0e.apigw.ntruss.com/custom/v1/29483/345ba9ece7db9b07eeeba3b0b32f252903887b5c2b5408ebfa3a0178fa9f371f"

def ocr_header(fn):
    def set_header(**kwargs):
        headers = {
            'X-OCR-SECRET': SECRET_KEY,
            'Content-Type': 'application/json'
        }
        kwargs["headers"] = headers
        res = fn(**kwargs)
        return res
    return set_header

@ocr_header
async def post_general_ocr(data: Images, headers: dict = {}):
    api_url = f"{OCR_URL}/{type}"
    image_url = data.url
    
    request_json = {
        'images': [
            {
                'format': 'jpg',
                'name': 'demo',
                'url': image_url,                
            }
        ],
        'requestId': str(uuid.uuid4()),
        'version': 'V2',   
        'timestamp': int(round(time.time() * 1000))
    }

    payload = json.dumps(request_json).encode('UTF-8')
    response = requests.request("POST", api_url, headers=headers, data = payload)

    return response

@ocr_header
def post_template_ocr(data: Images, headers: dict = {}, template_id = ""):
    api_url = f"{OCR_URL}/infer"
    image_url = data.url
    request_json = {
        "version": "V1",
        "requestId":str(uuid.uuid4()),
        "timestamp": 0,
        "lang":"ko",
        "images": [
            {
            "format": "jpg",
            "name": "test 1",
            "url": image_url,
            "templateIds":[int(template_id)]
            }
        ]
    }

    payload = json.dumps(request_json).encode('UTF-8')
    response = requests.request("POST", api_url, headers=headers, data = payload)
    res = json.loads(response.text.encode('utf8'))

    return res


def save_file(data, file_name = "result_mid.json"):
    with open(file_name, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)


def get_text(data: dict = {}):
    new_dicts = []

    for image in data['images']:
        for filed in image['fields']:
            new_dict = {"key": filed["name"], "value": filed['inferText']}
            new_dicts.append(new_dict)
    return new_dicts