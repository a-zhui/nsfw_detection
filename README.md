# NSFW检测 （色情检测）
> 使用huggingface上的nsfw模型，对 NSFW（工作不安全）图像进行分类。使其适合过滤各种应用程序中的露骨或不当内容。
> 
> ![image.png](images/image.png) 
> 
> [huggingface地址](https://huggingface.co/Falconsai/nsfw_image_detection)
> 
> 在Falconsai/nsfw_image_detection的基础上将其封装成api，并用gradio编写了一个简单的测试界面
> 
> api 测试详见项目api_test.py文件


## 使用方式一：python虚拟环境
> 安装 miniconda/anaconda
```bash
##构建虚拟环境
conda create -n nsfw_detection python=3.10
conda activate nsfw_detection

pip install torch
pip install transformers
pip install uvicorn
pip install gradio

```

```bash
##启动服务
uvicorn --host 0.0.0.0 --port 7860 main:app
```




## 使用方式二：docker
```bash
##启动服务
docker run -it -d -p 8080:7860 --restart always --workdir /root/nsfw_detection --name nsfw_detection nsfw_detection:V1.0 bash -c "bash init.sh"
```