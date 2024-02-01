import logging
from detection import execute
import gradio as gr
from api import app_api

logging.basicConfig(format='[%(filename)s:%(lineno)d] %(asctime)s - %(levelname)s : %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=20)


def ex(image):
    result_dic = execute(image)

    return image, result_dic, result_dic


ui = gr.Interface(fn=ex,
                  title='NSFW 图片检测（色情检测）',
                  inputs=[gr.Image(label='图片', type='pil')],
                  outputs=[gr.Image(label='输入', width=300, container=False), gr.Label(label='结果', container=False), gr.JSON(label='json output', container=False)],
                  allow_flagging='never',
                  examples=[['images/1.jpg'], ['images/2.jpg'], ['images/3.jpg']]
                  )

ui.queue()
ui.show_api = False
# ui.launch(inbrowser=True, server_name='0.0.0.0', server_port=7860)

# 将api与ui界面挂载,path为ui界面的访问路径
app = gr.mount_gradio_app(app_api, ui, path='/')
