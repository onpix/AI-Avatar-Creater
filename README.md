# AI-Avatar-Creater
使用生成对抗网络（`GAN`）和`CNN`在线生成个性化头像！

![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/hackweek/app/static/pic/bg-index.png)

***

## Contributors

* AI算法 & design：@creeper121386
* web开发：@Benjaminyuan
* 服务器部署：@ThinCats

***

## Introduction

你可以使用`AI-Avatar-Creater`来：

### 进行实时风格迁移

（论文见[这里](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf?spm=5176.100239.blogcont62518.12.e6rUdh&file=Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)），可以将用户上传的图片转换特定风格：
  
![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/2018-08-07%2010-35-08%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/2018-08-07%2010-35-11%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/2018-08-07%2010-35-17%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)

***

### 使用`GAN`生成动漫风格头像

* `LoveLive`风格头像的训练数据来自`LoveLive!`的人物立绘。
* 其他训练数据均来自各动漫图库。

### 生成效果

* 使用动漫图库训练的结果：

    ![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/sample-epoch41-test0.jpg)

* 使用网上下载的（别人爬的）数据集训练的结果，使用的模型结构来自`anime-GAN`：
  
    ![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/test_2.jpg)

* 使用lovelive立绘训练的结果：

    ![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/test.jpg)

    （忽略部分扭曲的五官...训练数据太少了没办法...毕竟还是有很多高质量头像的！可怜的why爬了整整两天的数据...

***

## To AI Developer

本产品是`UniqueHackweek`的参赛作品，不用做商业用途。如果你想要直接运行`PyTorch`神经网络或查看AI源码：
* 可以直接查看`AI-Avatar-Creater/hackweek/app/crawl/`和`AI-Avatar-Creater/hackweek/app/draw/`中的`pytorch`接口。
* 可以载入`AI-Avatar-Creater/hackweek/app/models`中的模型参数文件进行后续的训练或实验，训练数据可以使用爬虫自行爬取。

***

**Added by @ThinCats:**

## Build
To built, you need:
* NVIDIA with cuda-toolkit
* PyTorch
```sh
$ pip install pytorch
```
* Flask (for web view)
```sh
$ pip install flask
```
* Mataplotlib

## Run
1. Go to `hackweek` directory, and then run using `python manage.py`
2. It will download the PyTorch model automatically, wait patiently.
3. If successful, it should appear the basic server infomation. Go to http://localhost:5000 to have fun

## Future
Docker image(Still waited to be optimized)
