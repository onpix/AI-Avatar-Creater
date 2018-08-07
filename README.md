# AI-Avatar-Creater
使用生成对抗网络（`GAN`）和`CNN`在线生成个性化头像！

![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/hackweek/app/static/pic/bg-index.png)

***

## Contributors

AI算法 & design：@creeper121386
web开发：@Benjaminyuan
服务器部署：@ThinCats

***

## Introduction

你可以使用`AI-Avatar-Creater`来：

### 使用`GAN`生成动漫风格头像

* `LoveLive`风格头像的训练数据来自`LoveLive!`的人物立绘。
* 其他训练数据均来自各动漫图库。


### 使用实时风格迁移

（论文见[这里](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf?spm=5176.100239.blogcont62518.12.e6rUdh&file=Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)）可以将用户上传的图片转换特定风格：
  
![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/2018-08-07%2010-35-08%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/2018-08-07%2010-35-11%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)
![](https://raw.githubusercontent.com/creeper121386/AI-Avatar-Creater/master/debug_demo3_StyleTransfer/background/2018-08-07%2010-35-17%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)

***

## Built
To built, you need:
* PyTorch
    ```sh
    $ pip install pytorch
    ```
* NVIDIA with cuda-toolkit
* Flask (for web view)
```sh
$ pip install flask
```

## Run
1. Go to `hackweek` directory, and then run using `python manage.py`
2. It will download the PyTorch model automatically, wait patiently.
3. If successful, it should appear the basic server infomation. Go to http://localhost:5000 to have fun
