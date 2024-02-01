# 人脸自动贴国旗
> 使用opencv + dilb,通过dilb获取人脸关键点，然后简单的图像处理实现在右脸上贴国旗，刚好配合gradio写一个简单的demo
> 
> ![img.png](images/img.png) 
> 
> [博客地址](https://blog.csdn.net/weixin_43810267/article/details/132885775)


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