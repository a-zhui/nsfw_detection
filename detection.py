import logging
import time

from transformers import pipeline

classifier = pipeline("image-classification", model="nsfw_image_detection")


def execute(image):  # image 为pillow格式
    start_time = time.time()
    detection_result = classifier(image)
    logging.info(f'耗时约{round(time.time() - start_time, 2)}s,检测结果{detection_result}')
    result_dic = {}
    for i in detection_result:
        result_dic[i.get('label')] = i.get('score')
    return result_dic
