import base64
from io import BytesIO

from PIL import Image
from fastapi import FastAPI
from pydantic import BaseModel

from detection import execute

app_api = FastAPI()


class RequestData(BaseModel):
    image: str


class ResponseData(BaseModel):
    pass


@app_api.post('/api/nsfw_detection')
async def nsfw_detection(data: RequestData):

    byte_data = base64.b64decode(data.image)  # base64转bytes
    image = Image.open(BytesIO(byte_data))  # 将二进制转为PIL格式图片

    result_dic = execute(image)
    return result_dic
