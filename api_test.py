import base64

import requests


def backend_requests_post(url, json):
    headers = {'Connection': 'close', 'token': 'pass'}
    response = requests.post(url=url, json=json, headers=headers)
    json_data = response.json()
    return json_data


with open('images/1.jpg', 'rb') as f:
    content = f.read()

content = base64.b64encode(content)
content = content.decode()

ret = backend_requests_post(url='http://127.0.0.1:7860/api/nsfw_detection', json={
    'image': content
})
print(ret)
